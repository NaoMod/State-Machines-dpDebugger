from __future__ import annotations

import random
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
        state_machine (StateMachine): state machine on which execution is taking place.
        current_state (State): current state in the state machine.
        inputs (list[str]): ordered symbols given as inputs for the execution.
        next_consumed_input_index (int): index of the next input to consume.
        available_transitions (list[Transition]): list of transitions that can be fired.
    """

    def __init__(
        self, state_machine: stateMachineModule.StateMachine, inputs: list[str] | None
    ) -> None:
        self.state_machine: stateMachineModule.StateMachine = state_machine
        if state_machine.initial_state is None:
            raise ValueError("No initial state.")

        self.hasInputs = inputs is not None
        if self.hasInputs:
            self.inputs: list[str] = inputs
            self.next_consumed_input_index: int = 0

        self.current_state: stateMachineModule.State = (
            state_machine.initial_state.get_nested_initial_state()
        )
        self.variables: dict[str, float] = {}
        self.evaluator: ExpressionEvaluator = ExpressionEvaluator(self.variables)
        self.ongoing_composite_step: Step | None = None
        self.available_steps: dict[str, Step] | None = None

    def execute_step(self, step_id: str | None = None) -> AtomicStep:
        if step_id is None:
            if self.ongoing_composite_step is None:
                next_transition: stateMachineModule.Transition | None = (
                    self.find_next_transition()
                )
                assert next_transition is not None, "No transition to fire."
                selected_step: Step = TransitionStep(next_transition)
            else:
                selected_step: Step = self.ongoing_composite_step
        else:
            assert self.available_steps is not None, "No steps to compute from."
            assert step_id in self.available_steps, f"No step with id {step_id}."
            selected_step: Step = self.available_steps[step_id]

        atomic_step: AtomicStep = selected_step.get_next_atomic_step()
        atomic_step.execute(self)
        self.ongoing_composite_step = selected_step.find_ongoing_step()
        self.available_steps = None
        return atomic_step

    def compute_available_steps(self, step_id: str | None = None) -> dict[str, Step]:
        if self.hasInputs and self.next_consumed_input_index >= len(self.inputs):
            self.available_steps = {}
            return self.available_steps

        if step_id is None:
            # Only compute once for the same runtime state
            if self.available_steps is not None:
                return self.available_steps

            # Top-level steps are always transitions
            if self.ongoing_composite_step is None:
                self.available_steps = {}
                for t in self._find_possible_transitions():
                    step: TransitionStep = TransitionStep(t)
                    self.available_steps[step.id] = step

                return self.available_steps
            else:
                self.available_steps = {
                    step.id: step
                    for step in self.ongoing_composite_step.get_possible_steps()
                }
                return self.available_steps
        else:
            assert (
                self.available_steps is not None
            ), "No available steps to compute from."
            assert step_id in self.available_steps, f"No step with id {step_id}."
            self.available_steps = {
                step.id: step
                for step in self.available_steps[step_id].get_possible_steps()
            }
            return self.available_steps

    def find_next_transition(self) -> stateMachineModule.Transition | None:
        if self.hasInputs and self.next_consumed_input_index >= len(self.inputs):
            return None

        possibleSourceStates: list[stateMachineModule.State] = []
        state: stateMachineModule.State | None = self.current_state

        while state is not None:
            if len(state.outgoing_transitions) > 0:
                possibleSourceStates.append(state)

            state = state.parent_state

        if len(possibleSourceStates) == 0:
            return None

        stateIndex: int = random.randint(0, len(possibleSourceStates) - 1)
        transitionIndex: int = random.randint(
            0, len(possibleSourceStates[stateIndex].outgoing_transitions) - 1
        )
        return possibleSourceStates[stateIndex].outgoing_transitions[transitionIndex]

    def check_breakpoint(
        self, type: str, element_id: str, step_id: str | None = None
    ) -> lrpModule.CheckBreakpointResponse:
        if type not in [x.id for x in breakpoints]:
            raise UnknownBreakpointTypeError(type)

        if step_id is None:
            if self.ongoing_composite_step is None:
                next_transition: stateMachineModule.Transition | None = (
                    self.find_next_transition()
                )
                selected_step: Step | None = (
                    TransitionStep(next_transition)
                    if next_transition is not None
                    else None
                )
            else:
                selected_step: Step | None = self.ongoing_composite_step
        else:
            assert self.available_steps is not None, "No steps to compute from."
            assert step_id in self.available_steps, f"No step with id {step_id}."
            selected_step: Step | None = self.available_steps[step_id]

        if selected_step is None:
            return lrpModule.CheckBreakpointResponse(False)

        message: str | None = selected_step.get_next_atomic_step().check_breakpoint(
            type, element_id, self
        )
        is_activated = message is not None

        return lrpModule.CheckBreakpointResponse(is_activated, message)

    def _find_possible_transitions(self) -> list[stateMachineModule.Transition]:
        available_transitions: list[stateMachineModule.Transition] = []
        state: stateMachineModule.State | None = self.current_state

        while state is not None:
            for transition in state.outgoing_transitions:
                available_transitions.append(transition)

            state = state.parent_state

        return available_transitions

    def evaluate(self, expression: stateMachineModule.Expression) -> float:
        return self.evaluator.evaluate(expression)


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
        return expression.contained_expression.accept(self)

    def evaluate_variable_atomic_expression(
        self, expression: stateMachineModule.VariableAtomicExpression
    ) -> float:
        if expression.sign is stateMachineModule.Sign.MINUS:
            return -self.variables[expression.variable]

        return self.variables[expression.variable]

    def evaluate_number_atomic_expression(
        self, expression: stateMachineModule.NumberAtomicExpression
    ) -> float:
        if expression.sign is stateMachineModule.Sign.MINUS:
            return -expression.number

        return expression.number


@dataclass
class Step:
    name: str
    is_composite: bool
    id: str = field(default_factory=generate_uuid)
    description: str | None = None
    parent_step: CompositeStep | None = None
    location: lrpModule.Location | None = None

    @abstractmethod
    def get_next_atomic_step(self) -> AtomicStep:
        pass

    @abstractmethod
    def is_completed(self) -> bool:
        pass

    @abstractmethod
    def get_possible_steps(self) -> list[Step]:
        pass

    @abstractmethod
    def check_breakpoint(
        self, type: str, element_id: str, runtime: Runtime
    ) -> str | None:
        pass

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
        id: str | None = None,
        description: str | None = None,
        parent_step: Step | None = None,
        location: lrpModule.Location | None = None,
    ) -> None:
        super().__init__(
            name,
            False,
            generate_uuid() if id is None else id,
            description,
            parent_step,
            location,
        )
        self._is_completed: bool = False

    def is_completed(self) -> bool:
        return self._is_completed

    def get_possible_steps(self) -> list[Step]:
        assert False, "Shouldn't be called."

    def get_next_atomic_step(self) -> AtomicStep:
        return self

    def get_completed_steps(self) -> list[Step]:
        result: list[Step] = [] if not self.is_completed() else [self]
        parent_step: Step | None = self.parent_step
        while parent_step is not None:
            if not parent_step.is_completed():
                break

            result.append(parent_step)
            parent_step = parent_step.parent_step

        return result

    @abstractmethod
    def execute(self, runtime: Runtime) -> None:
        pass


class CompositeStep(Step):
    def __init__(
        self,
        name: str,
        id: str | None = None,
        description: str | None = None,
        parent_step: Step | None = None,
        location: lrpModule.Location | None = None,
    ) -> None:
        super().__init__(
            name,
            True,
            generate_uuid() if id is None else id,
            description,
            parent_step,
            location,
        )

    @abstractmethod
    def child_step_completed(self):
        pass


class TransitionStep(CompositeStep):
    def __init__(self, transition: stateMachineModule.Transition) -> None:
        target: str = "FINAL" if transition.target.is_final else transition.target.name
        super().__init__(
            f"{transition.source.name} --'{transition.input}'--> {target}",
            location=transition.step_location,
        )
        self.transition = transition
        self.next_assignment_index: int = 0
        self.assignements_done: bool = len(transition.assignments) == 0
        self.state_changed: bool = False

    def is_completed(self) -> bool:
        return self.assignements_done and self.state_changed

    def get_next_atomic_step(self) -> AtomicStep:
        if not self.assignements_done:
            next_assignment: stateMachineModule.Assignment = (
                self.transition.assignments[self.next_assignment_index]
            )
            return AssignmentStep(next_assignment, self)

        if not self.state_changed:
            return StateChangeStep(self.transition.target, self)

        assert False, "Step already completed."

    def get_possible_steps(self) -> list[Step]:
        if not self.assignements_done:
            return [
                AssignmentStep(
                    self.transition.assignments[self.next_assignment_index], self
                )
            ]

        if not self.state_changed:
            return [
                StateChangeStep(self.transition.target, self)
            ]

        assert False, "Step already completed."

    def child_step_completed(self):
        if not self.assignements_done:
            self.next_assignment_index += 1
            self.assignements_done = self.next_assignment_index >= len(
                self.transition.assignments
            )
            return

        if not self.state_changed:
            self.state_changed = True
            return

        assert False, "Step already completed."

    def check_breakpoint(
        self, type: str, element_id: str, runtime: Runtime
    ) -> str | None:
        if type == "stateMachine.transitionFired":
            return (
                f"Transition {self.transition.source.name} -> {self.transition.target.name} is about to be fired."
                if self.transition.id == element_id
                else None
            )

        return None


class AssignmentStep(AtomicStep):
    def __init__(
        self, assignment: stateMachineModule.Assignment, parent_step: TransitionStep
    ) -> None:
        super().__init__(
            f"{assignment.variable} = {assignment.expression.value()}",
            parent_step=parent_step,
            location=assignment.step_location,
        )
        self.assignment = assignment

    def execute(self, runtime: Runtime) -> None:
        runtime.variables[self.assignment.variable] = runtime.evaluate(
            self.assignment.expression
        )

        self.parent_step.child_step_completed()
        self._is_completed = True

    def check_breakpoint(
        self, type: str, element_id: str, runtime: Runtime
    ) -> str | None:
        if type == "stateMachine.assignmentEvaluated":
            return (
                f"Assignment {self.assignment.variable} = {self.assignment.expression.value()} is about to be evaluated."
                if self.assignment.id == element_id
                else None
            )

        return self.parent_step.check_breakpoint(type, element_id, runtime)


class StateChangeStep(AtomicStep):
    def __init__(
        self,
        target: stateMachineModule.State,
        parent_step: TransitionStep,
    ) -> None:
        super().__init__(
            f"New state: {target.name}", parent_step=parent_step
        )
        self.target = target

    def execute(self, runtime: Runtime) -> None:
        runtime.current_state = self.target.get_nested_initial_state()

        if runtime.hasInputs:
            runtime.next_consumed_input_index += 1

        self.parent_step.child_step_completed()
        self._is_completed = True

    def check_breakpoint(
        self, type: str, element_id: str, runtime: Runtime
    ) -> str | None:
        if type == "stateMachine.stateReached":
            state: stateMachineModule.State | None = self._find_reached_state(
                self.target, element_id
            )
            return (
                f"State {state.name} is about to be reached."
                if state is not None
                else None
            )

        if type == "stateMachine.stateExited":
            state: stateMachineModule.State | None = self._find_exited_state(
                runtime.current_state, self.parent_step.transition.source, element_id
            )
            return (
                f"State {state.name} is about to be exited."
                if state is not None
                else None
            )

        return self.parent_step.check_breakpoint(type, element_id, runtime)

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


class RuntimeState(lrpModule.ModelElement):
    """Represents the current state of a runtime.
    Contains the information passed to the debugger.

    Attributes:
        inputs (list[str]): ordered symbols given as inputs for the execution.
        next_consumed_input_index (int | None): index of the next input to consume. None if there is no input left.
        current_state (State): current state in the state machine.
    """

    def __init__(self, runtime: Runtime) -> None:
        super().__init__("stateMachine.runtimeState")
        self.current_state = runtime.current_state
        self.variables = runtime.variables
        self.hasInputs = runtime.hasInputs
        if runtime.hasInputs:
            self.inputs = runtime.inputs
            self.next_consumed_input_index = runtime.next_consumed_input_index

    def to_dict(self) -> dict:
        if self.current_state.is_final:
            attributes: dict = {"currentState": "FINAL"}
            if self.hasInputs:
                attributes["inputs"] = self.inputs
                attributes["nextConsumedInputIndex"] = self.next_consumed_input_index

            return super().construct_dict(
                attributes,
                {"variables": VariablesRegistry(self.variables).to_dict()},
                {},
            )

        attributes: dict = {}
        if self.hasInputs:
            attributes["inputs"] = self.inputs
            attributes["nextConsumedInputIndex"] = self.next_consumed_input_index

        return super().construct_dict(
            attributes,
            {"variables": VariablesRegistry(self.variables).to_dict()},
            {"currentState": self.current_state.id},
        )


class VariablesRegistry(lrpModule.ModelElement):
    def __init__(self, variables: dict[str, float]) -> None:
        super().__init__("stateMachine.variablesRegistry")
        self.variables = variables

    def to_dict(self) -> dict:
        return super().construct_dict(self.variables, {}, {})
