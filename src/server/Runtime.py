from __future__ import annotations

import statemachine_ast.StateMachine as stateMachineModule

import server.LRP as lrpModule
from server.ServerExceptions import (ExecutionAlreadyDoneError,
                                     UnknownBreakpointTypeError)


class Runtime:
    """Keeps track of the current runtime state for a given program.

    Attributes:
        state_machine (StateMachine): state machine on which execution is taking place.
        current_state (State): current state in the state machine.
        inputs (list[str]): ordered symbols given as inputs for the execution.
        next_consumed_input_index (int): index of the next input to consume.
        outputs (list[str]): outputs created so far during the execution.
        next_transition (Transition): next transition to be fired.
    """

    def __init__(self, state_machine: stateMachineModule.StateMachine, inputs: list[str]) -> None:
        self.state_machine: stateMachineModule.StateMachine = state_machine
        if state_machine.initial_state is None:
            raise ValueError('No initial state.')

        self.inputs: list[str] = inputs
        self.outputs: list[str] = []
        self.next_consumed_input_index: int = 0
        self.current_state: stateMachineModule.State = state_machine.initial_state.get_nested_initial_state()
        self.next_transition: stateMachineModule.Transition | None = self._find_next_transition()

    def next_step(self) -> stateMachineModule.Transition | None:
        if self.next_transition is None:
            raise ExecutionAlreadyDoneError()

        self.current_state = self.next_transition.target.get_nested_initial_state()
        self.next_consumed_input_index += 1
        self.outputs.append(self.next_transition.output)
        self.next_transition = self._find_next_transition()

        return self.next_transition

    def _find_next_transition(self) -> stateMachineModule.Transition | None:
        if self.next_consumed_input_index >= len(self.inputs):
            return None

        state: stateMachineModule.State | None = self.current_state

        while state is not None:
            for transition in state.outgoing_transitions:
                if transition.input == self.inputs[self.next_consumed_input_index]:
                    return transition

            state = state.parent_state

        return None

    def check_breakpoint(self, type: str, element_id: str) -> lrpModule.CheckBreakpointResponse:
        if self.next_transition is None:
            return lrpModule.CheckBreakpointResponse(False)

        is_activated = False
        message: str = ''

        match type:
            case 'stateMachine.transitionFired':
                is_activated = self.next_transition.id == element_id
                if is_activated:
                    message = f'Transition {self.next_transition.source.name} -> {self.next_transition.target.name} is about to be fired.'

            case 'stateMachine.stateReached':
                state: stateMachineModule.State | None = self._find_reached_state(
                    self.next_transition.target, element_id)
                is_activated = state is not None
                if is_activated:
                    message = f'State {state.name} is about to be reached.'

            case 'stateMachine.stateExited':
                state: stateMachineModule.State | None = self._find_exited_state(
                    self.current_state, self.next_transition.source, element_id)
                is_activated = state is not None
                if is_activated:
                    message = f'State {state.name} is about to be exited.'

            case _:
                raise UnknownBreakpointTypeError(type)

        return lrpModule.CheckBreakpointResponse(is_activated, message if is_activated else None)

    def _find_exited_state(self, current_state: stateMachineModule.State, transition_source: stateMachineModule.State, state_id_to_match: str) -> stateMachineModule.State | None:
        if current_state.id == state_id_to_match:
            return current_state

        if current_state.id == transition_source.id or current_state.parent_state is None:
            return None

        return self._find_exited_state(current_state.parent_state, transition_source, state_id_to_match)

    def _find_reached_state(self, parent_state: stateMachineModule.State, state_id_to_match: str) -> stateMachineModule.State | None:
        if parent_state.id == state_id_to_match:
            return parent_state

        current_state: stateMachineModule.State | None = parent_state.get_nested_initial_state()

        while current_state is not parent_state and current_state is not None:
            if current_state.id == state_id_to_match:
                return current_state

            current_state = current_state.parent_state

        return None
