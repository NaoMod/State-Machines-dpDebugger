from __future__ import annotations

from abc import abstractmethod
from dataclasses import dataclass, field

import server.LRP as lrpModule
import statemachine_ast.StateMachine as stateMachineModule
from server.ExposedTypes import breakpoints
from server.ServerExceptions import UnknownBreakpointTypeError
from server.Utils import generate_uuid


class Runtime:
    """Keeps track of the current runtime state for a given program.

    Attributes:
        TODO
    """

    def __init__(self, state_machine: stateMachineModule.StateMachine) -> None:
        self.state_machine: stateMachineModule.StateMachine = state_machine
        if state_machine.initial_state is None:
            raise ValueError("No initial state.")

        self.current_event: str | None = None
        self.current_transition: stateMachineModule.Transition | None = None
        self.executed_assignments: int = 0

        self.current_state: stateMachineModule.State = (
            state_machine.initial_state.get_nested_initial_state()
        )
        self.variables: dict[str, float] = {}
        self.evaluator: ExpressionEvaluator = ExpressionEvaluator(self.variables)

        self.ongoing_composite_step: Step | None = None
        self.available_steps: dict[str, Step] | None = None

    def execute_atomic_step(self, step_id: str) -> AtomicStep:
        assert self.available_steps is not None, "No steps to compute from."
        assert step_id in self.available_steps, f"No step with id {step_id}."
        selected_step: Step = self.available_steps[step_id]
        assert not selected_step.is_completed(), "Step already completed."

        selected_step.execute()
        self.ongoing_composite_step = selected_step.find_ongoing_step()
        self.available_steps = None
        return selected_step

    def enter_composite_step(self, step_id: str) -> None:
        assert self.available_steps is not None, "No steps to compute from."
        assert step_id in self.available_steps, f"No step with id {step_id}."
        selected_step: Step = self.available_steps[step_id]
        assert selected_step.is_composite, "Step must be composite."

        self.ongoing_composite_step = selected_step
        self.available_steps = None

    def compute_available_steps(self) -> dict[str, Step]:
        # Only compute once for the same runtime state
        if self.available_steps is not None:
            return self.available_steps

        if self.current_state.is_final:
            self.available_steps = {}
            return self.available_steps

        # Top-level steps
        if self.ongoing_composite_step is None:
            self.available_steps = {}
            if self.current_event is None:
                for event in self._find_possible_events():
                    step: ActivateEventStep = ActivateEventStep(event, self)
                    self.available_steps[step.id] = step

            else:
                for transition in self._find_possible_transitions(self.current_event):
                    step: TransitionStep = TransitionStep(transition, self)
                    self.available_steps[step.id] = step

        else:
            self.available_steps = {
                step.id: step
                for step in self.ongoing_composite_step.get_contained_steps()
            }

        return self.available_steps

    def check_breakpoint(
        self, type_id: str, step_id: str, entries: dict
    ) -> lrpModule.CheckBreakpointResponse:
        if type_id not in [x.id for x in breakpoints]:
            raise UnknownBreakpointTypeError(type_id)

        assert self.available_steps is not None, "No steps to compute from."
        assert step_id in self.available_steps, f"No step with id {step_id}."
        selected_step: Step = self.available_steps[step_id]

        message: str | None = selected_step.check_breakpoint(type_id, entries)
        is_activated = message is not None

        return lrpModule.CheckBreakpointResponse(is_activated, message)

    def evaluate(self, expression: stateMachineModule.Expression) -> float:
        return self.evaluator.evaluate(expression)

    def _find_possible_events(self) -> list[str]:
        available_transitions: list[stateMachineModule.Transition] = (
            self._find_possible_transitions()
        )
        events: set[str] = set()

        for t in available_transitions:
            events.add(t.trigger)

        return list(events)

    def _find_possible_transitions(
        self, event: str | None = None
    ) -> list[stateMachineModule.Transition]:
        available_transitions: list[stateMachineModule.Transition] = []
        state: stateMachineModule.State | None = self.current_state

        while state is not None:
            for transition in state.outgoing_transitions:
                if event is None or event == transition.trigger:
                    available_transitions.append(transition)

            state = state.parent_state

        return available_transitions


@dataclass
class ExpressionEvaluator:
    variables: dict[str, float]

    def evaluate(self, expression: stateMachineModule.Expression) -> float:
        return expression.accept(self)

    def evaluate_binary_expression(
        self, expression: stateMachineModule.BinaryExpression
    ) -> float:
        evaluated_left: float = expression.left.accept(self)
        evaluated_right: float = expression.right.accept(self)
        match expression.operand:
            case stateMachineModule.Operand.POW:
                return evaluated_left ^ evaluated_right
            case stateMachineModule.Operand.TIMES:
                return evaluated_left * evaluated_right
            case stateMachineModule.Operand.DIV:
                return evaluated_left / evaluated_right
            case stateMachineModule.Operand.PLUS:
                return evaluated_left + evaluated_right
            case stateMachineModule.Operand.MINUS:
                return evaluated_left - evaluated_right

    def evaluate_parenthesized_expression(
        self, expression: stateMachineModule.ParenthesizedExpression
    ) -> float:
        unsigned_result: int = expression.contained_expression.accept(self)
        return (
            -unsigned_result
            if expression.sign is stateMachineModule.Sign.MINUS
            else unsigned_result
        )

    def evaluate_variable_atomic_expression(
        self, expression: stateMachineModule.VariableAtomicExpression
    ) -> float:
        unsigned_result: int = self.variables[expression.variable]
        return (
            -unsigned_result
            if expression.sign is stateMachineModule.Sign.MINUS
            else unsigned_result
        )

    def evaluate_number_atomic_expression(
        self, expression: stateMachineModule.NumberAtomicExpression
    ) -> float:
        unsigned_result: int = expression.number
        return (
            -unsigned_result
            if expression.sign is stateMachineModule.Sign.MINUS
            else unsigned_result
        )


@dataclass
class Step:
    name: str
    is_composite: bool
    runtime: Runtime
    id: str = field(default_factory=generate_uuid)
    description: str | None = None
    parent_step: Step | None = None
    location: lrpModule.Location | None = None

    @abstractmethod
    def is_completed(self) -> bool:
        pass

    @abstractmethod
    def get_contained_steps(self) -> list[Step]:
        pass

    @abstractmethod
    def check_breakpoint(self, type: str, entries: dict) -> str | None:
        pass

    @abstractmethod
    def execute(self) -> None:
        pass

    def get_completed_steps(self) -> list[Step]:
        result: list[Step] = [] if not self.is_completed() else [self]
        parent_step: Step | None = self.parent_step
        while parent_step is not None:
            if not parent_step.is_completed():
                break

            result.append(parent_step)
            parent_step = parent_step.parent_step

        return result

    def find_ongoing_step(self) -> Step | None:
        if not self.is_completed():
            return self

        return (
            None if self.parent_step is None else self.parent_step.find_ongoing_step()
        )

    def to_LRP_step(self) -> lrpModule.Step:
        return lrpModule.Step(self.id, self.name, self.is_composite, self.description)


class AtomicStep(Step):
    def __init__(
        self,
        name: str,
        runtime: Runtime,
        id: str | None = None,
        description: str | None = None,
        parent_step: Step | None = None,
        location: lrpModule.Location | None = None,
    ) -> None:
        super().__init__(
            name,
            False,
            runtime,
            generate_uuid() if id is None else id,
            description,
            parent_step,
            location,
        )
        self._is_completed: bool = False

    def is_completed(self) -> bool:
        return self._is_completed

    def get_contained_steps(self) -> list[Step]:
        assert False, "Step must be composite."


class CompositeStep(Step):
    def __init__(
        self,
        name: str,
        runtime: Runtime,
        id: str | None = None,
        description: str | None = None,
        parent_step: Step | None = None,
        location: lrpModule.Location | None = None,
    ) -> None:
        super().__init__(
            name,
            True,
            runtime,
            generate_uuid() if id is None else id,
            description,
            parent_step,
            location,
        )

    def execute(self) -> None:
        assert False, "Step must be atomic."


class TransitionStep(CompositeStep):
    def __init__(
        self, transition: stateMachineModule.Transition, runtime: Runtime
    ) -> None:
        target: str = "FINAL" if transition.target.is_final else transition.target.name
        step_location: lrpModule.Location = lrpModule.Location(
            transition.location.line,
            transition.parser_ctx.stop.line,
            transition.location.column,
            transition.parser_ctx.stop.column
            + len(transition.parser_ctx.stop.text)
            + 1,
        )

        super().__init__(
            f"{transition.source.name} --'{transition.trigger}'--> {target}",
            runtime,
            description="fireTransition",
            location=step_location,
        )
        self.transition = transition

    def is_completed(self) -> bool:
        return self.runtime.current_event is None

    def get_contained_steps(self) -> list[Step]:
        if self.runtime.current_transition is None:
            return [ActivateTransitionStep(self.transition, self, self.runtime)]

        if self.runtime.executed_assignments < len(self.transition.assignments):
            return [
                ExecuteAssignmentStep(
                    self.transition.assignments[self.runtime.executed_assignments],
                    self,
                    self.runtime,
                )
            ]

        if self.runtime.current_event is not None:
            return [StateChangeStep(self, self.runtime)]

        assert False, "Step already completed."

    def check_breakpoint(self, type: str, entries: dict) -> str | None:
        if type == "transitionFired":
            return (
                f"Transition {self.transition.label} is about to be fired."
                if self.transition.id == entries["t"]
                else None
            )


class ActivateEventStep(AtomicStep):
    def __init__(self, event: str, runtime: Runtime) -> None:
        super().__init__(
            event,
            runtime,
            description="activateEvent",
        )
        self.event = event

    def execute(self) -> None:
        self.runtime.current_event = self.event
        self._is_completed = True

    def check_breakpoint(self, type: str, entries: dict) -> str | None:
        return


class ActivateTransitionStep(AtomicStep):
    def __init__(
        self,
        transition: stateMachineModule.Transition,
        parent_step: TransitionStep,
        runtime: Runtime,
    ) -> None:
        target: str = "FINAL" if transition.target.is_final else transition.target.name
        step_location: lrpModule.Location = lrpModule.Location(
            transition.location.line,
            transition.parser_ctx.stop.line,
            transition.location.column,
            transition.parser_ctx.stop.column
            + len(transition.parser_ctx.stop.text)
            + 1,
        )

        super().__init__(
            f"{transition.source.name} --'{transition.trigger}'--> {target}",
            runtime,
            description="activateTransition",
            parent_step=parent_step,
            location=step_location,
        )
        self.transition = transition

    def execute(self) -> None:
        self.runtime.current_transition = self.transition
        self._is_completed = True

    def check_breakpoint(self, type: str, entries: dict) -> str | None:
        return


class ExecuteAssignmentStep(AtomicStep):
    def __init__(
        self,
        assignment: stateMachineModule.Assignment,
        parent_step: TransitionStep,
        runtime: Runtime,
    ) -> None:
        step_location: lrpModule.Location = lrpModule.Location(
            assignment.location.line,
            assignment.location.endLine,
            assignment.location.column,
            assignment.location.endColumn + 1,
        )

        super().__init__(
            f"{assignment.variable} = {assignment.expression.value()}",
            runtime,
            description="executeAssignement",
            parent_step=parent_step,
            location=step_location,
        )
        self.assignment = assignment

    def execute(self) -> None:
        self.runtime.variables[self.assignment.variable] = self.runtime.evaluate(
            self.assignment.expression
        )
        self.runtime.executed_assignments += 1
        self._is_completed = True

    def check_breakpoint(self, type: str, entries: dict) -> str | None:
        if type == "assignmentExecuted":
            return (
                f"Assignment {self.assignment.label} is about to be executed."
                if self.assignment.id == entries["a"]
                else None
            )


class StateChangeStep(AtomicStep):
    def __init__(self, parent_step: TransitionStep, runtime: Runtime) -> None:
        self.source: stateMachineModule.State = runtime.current_transition.source
        self.target: stateMachineModule.State = runtime.current_transition.target
        super().__init__(
            f"New state: {self.target.name}", runtime, parent_step=parent_step
        )

    def execute(self) -> None:
        self.runtime.current_state = self.target.get_nested_initial_state()
        self.runtime.current_event = None
        self.runtime.current_transition = None
        self.runtime.executed_assignments = 0

        self._is_completed = True

    def check_breakpoint(self, type: str, entries: dict) -> str | None:
        if type == "stateReached":
            state: stateMachineModule.State | None = self._find_reached_state(
                self.target, entries["s"]
            )
            return (
                f"State {state.name} is about to be reached."
                if state is not None
                else None
            )

        if type == "stateExited":
            state: stateMachineModule.State | None = self._find_exited_state(
                self.runtime.current_state, self.source, entries["s"]
            )
            return (
                f"State {state.name} is about to be exited."
                if state is not None
                else None
            )

    def _find_reached_state(
        self, parent_state: stateMachineModule.State, state_id_to_match: str
    ) -> stateMachineModule.State | None:
        if parent_state.id == state_id_to_match:
            return parent_state

        current_state: stateMachineModule.State | None = (
            parent_state.get_nested_initial_state()
        )

        while current_state is not parent_state and current_state is not None:
            if current_state.id == state_id_to_match:
                return current_state

            current_state = current_state.parent_state

        return None

    def _find_exited_state(
        self,
        current_state: stateMachineModule.State,
        transition_source: stateMachineModule.State,
        state_id_to_match: str,
    ) -> stateMachineModule.State | None:
        if current_state.id == state_id_to_match:
            return current_state

        if (
            current_state.id == transition_source.id
            or current_state.parent_state is None
        ):
            return None

        return self._find_exited_state(
            current_state.parent_state, transition_source, state_id_to_match
        )


class RuntimeState:
    """Represents the current state of a runtime.
    Contains the information passed to the debugger.

    Attributes:
        TODO
    """

    def __init__(self, runtime: Runtime) -> None:
        self.current_state = runtime.current_state
        self.variables = runtime.variables
        self.current_event: str | None = runtime.current_event

    def to_model_element(self) -> lrpModule.ModelElement:
        if self.current_state.is_final:
            attributes: dict = {"currentState": "FINAL"}
            if self.current_event:
                attributes["currentEvent"] = self.current_event

            return lrpModule.ModelElement(
                generate_uuid(),
                ["RuntimeState"],
                attributes,
                {"variables": VariablesRegistry(self.variables).to_model_element()},
                {},
            )

        attributes: dict = {}
        if self.current_event:
            attributes["currentEvent"] = self.current_event

        return lrpModule.ModelElement(
            generate_uuid(),
            ["RuntimeState"],
            attributes,
            {"variables": VariablesRegistry(self.variables).to_model_element()},
            {"currentState": self.current_state.id},
        )


class VariablesRegistry:
    def __init__(self, variables: dict[str, float]) -> None:
        self.variables = variables

    def to_model_element(self) -> dict:
        return lrpModule.ModelElement(
            generate_uuid(), ["VariablesRegistry"], self.variables, {}, {}
        )
