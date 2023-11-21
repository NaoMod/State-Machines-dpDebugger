from __future__ import annotations

from dataclasses import dataclass

import server.LRP as lrpModule
import statemachine_ast.StateMachine as stateMachineModule
from server.ServerExceptions import UnknownBreakpointTypeError


class Runtime:
    """Keeps track of the current runtime state for a given program.

    Attributes:
        state_machine (StateMachine): state machine on which execution is taking place.
        current_state (State): current state in the state machine.
        inputs (list[str]): ordered symbols given as inputs for the execution.
        next_consumed_input_index (int): index of the next input to consume.
        outputs (list[str]): outputs created so far during the execution.
        available_transitions (list[Transition]): list of transitions that can be fired.
    """

    def __init__(
        self, state_machine: stateMachineModule.StateMachine, inputs: list[str]
    ) -> None:
        self.state_machine: stateMachineModule.StateMachine = state_machine
        if state_machine.initial_state is None:
            raise ValueError("No initial state.")

        self.inputs: list[str] = inputs
        self.outputs: list[str] = []
        self.next_consumed_input_index: int = 0
        self.current_state: stateMachineModule.State = (
            state_machine.initial_state.get_nested_initial_state()
        )
        self.variables: dict[str, float] = {}
        self.evaluator: ExpressionEvaluator = ExpressionEvaluator(self.variables)
        self.available_transitions: list[stateMachineModule.Transition] | None = None

    def execute_step(self, stepId: str | None = None) -> None:
        next_transition: stateMachineModule.Transition | None = (
            self.find_next_transition()
            if stepId is None
            else self.available_transitions[stepId]
        )

        assert next_transition is not None, "No transition to fire."
        self._fire_transition(next_transition)
        self.available_transitions = None

    def compute_available_transitions(self) -> list[stateMachineModule.Transition]:
        if self.next_consumed_input_index >= len(self.inputs):
            return []

        available_transitions: list[stateMachineModule.Transition] = []
        state: stateMachineModule.State | None = self.current_state

        while state is not None:
            for transition in state.outgoing_transitions:
                if transition.input == self.inputs[self.next_consumed_input_index]:
                    available_transitions.append(transition)

            state = state.parent_state

        return available_transitions

    def find_next_transition(self) -> stateMachineModule.Transition | None:
        if self.next_consumed_input_index >= len(self.inputs):
            return None

        state: stateMachineModule.State | None = self.current_state

        while state is not None:
            for transition in state.outgoing_transitions:
                if transition.input == self.inputs[self.next_consumed_input_index]:
                    return transition

            state = state.parent_state

        return None

    def check_breakpoint(
        self, type: str, element_id: str, stepId: str | None = None
    ) -> lrpModule.CheckBreakpointResponse:
        next_transition: stateMachineModule.Transition | None = (
            self.find_next_transition()
            if stepId is None
            else self.available_transitions[stepId]
        )

        if next_transition is None:
            return lrpModule.CheckBreakpointResponse(False)

        is_activated = False
        message: str = ""

        match type:
            case "stateMachine.transitionFired":
                is_activated = next_transition.id == element_id
                if is_activated:
                    message = f"Transition {next_transition.source.name} -> {next_transition.target.name} is about to be fired."

            case "stateMachine.stateReached":
                state: stateMachineModule.State | None = self._find_reached_state(
                    next_transition.target, element_id
                )
                is_activated = state is not None
                if state is not None:
                    message = f"State {state.name} is about to be reached."

            case "stateMachine.stateExited":
                state: stateMachineModule.State | None = self._find_exited_state(
                    self.current_state, next_transition.source, element_id
                )
                is_activated = state is not None
                if state is not None:
                    message = f"State {state.name} is about to be exited."

            case _:
                raise UnknownBreakpointTypeError(type)

        return lrpModule.CheckBreakpointResponse(
            is_activated, message if is_activated else None
        )

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

    def _fire_transition(self, transition: stateMachineModule.Transition) -> None:
        if transition.assignments is not None:
            for assignment in transition.assignments:
                self.variables[assignment.variable] = self.evaluator.evaluate(
                    assignment.expression
                )

        self.current_state = transition.target.get_nested_initial_state()
        self.next_consumed_input_index += 1
        if transition.output is not None:
            self.outputs.append(transition.output)


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
