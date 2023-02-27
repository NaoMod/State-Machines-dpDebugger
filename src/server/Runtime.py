from __future__ import annotations

import statemachine_ast.StateMachine as stateMachineModule

import server.LRP as lrpModule


class Runtime:
    """Keeps track of the current runtime state for a given program.

    Attributes:
        stateMachine (statemachine_ls.statemachine_ast.StateMachine.StateMachine): State machine on which execution is taking place.
        currentState (statemachine_ls.statemachine_ast.StateMachine.State): Current state in the state machine.
        inputs (list[str]): Ordered symbols given as inputs for the execution.
        nextConsumedInputIndex (int): Index of the next input to consume.

    """

    def __init__(self, stateMachine: stateMachineModule.StateMachine, inputs: list[str]) -> None:
        self.stateMachine: stateMachineModule.StateMachine = stateMachine
        if stateMachine.initialState is None:
            raise Exception('No initial state.')

        self.inputs: list[str] = inputs
        self.outputs: list[str] = []
        self.nextConsumedInputIndex: int = 0
        self.currentState: stateMachineModule.State = stateMachine.initialState.getNestedInitialState()
        self.nextTransition: stateMachineModule.Transition | None = self._findNextTransition()

    def nexStep(self) -> stateMachineModule.Transition | None:
        if self.nextTransition is None:
            raise Exception('Execution already done.')

        self.currentState = self.nextTransition.target.getNestedInitialState()
        self.nextConsumedInputIndex += 1
        self.outputs.append(self.nextTransition.output)
        self.nextTransition = self._findNextTransition()

        return self.nextTransition

    def _findNextTransition(self) -> stateMachineModule.Transition | None:
        if self.nextConsumedInputIndex >= len(self.inputs):
            return None

        state: stateMachineModule.State | None = self.currentState

        while not state is None:
            for transition in state.outgoingTransitions:
                if transition.input == self.inputs[self.nextConsumedInputIndex]:
                    return transition

            state = state.parentState

        return None

    def checkBreakpoint(self, type: str, elementId: str) -> lrpModule.CheckBreakpointResponse:
        if self.nextTransition is None:
            return lrpModule.CheckBreakpointResponse(False)

        isActivated = False
        message: str = ''

        match type:
            case 'stateMachine.transitionFired':
                isActivated = self.nextTransition.id == elementId
                if isActivated:
                    message = f'Transition {self.nextTransition.source.name} -> {self.nextTransition.target.name} is about to be fired.'

            case 'stateMachine.stateReached':
                state: stateMachineModule.State | None = self._findReachedState(
                    self.nextTransition.target, elementId)
                isActivated = not state is None
                if isActivated:
                    message = f'State {state.name} is about to be reached.'

            case 'stateMachine.stateExited':
                state: stateMachineModule.State | None = self._findExitedState(self.currentState, self.nextTransition.source, elementId)
                isActivated = not state is None
                if isActivated:
                    message = f'State {state.name} is about to be exited.'

            case _:
                raise Exception('Unknown breakpoint type ' + type + '.')

        return lrpModule.CheckBreakpointResponse(isActivated, message if isActivated else None)

    def _findExitedState(self, currentState: stateMachineModule.State, transitionSource: stateMachineModule.State, stateIdToMatch: str) ->  stateMachineModule.State | None:
        if currentState.id == stateIdToMatch:
            return currentState

        if currentState.id == transitionSource.id or currentState.parentState is None:
            return None

        return  self._findExitedState(currentState.parentState, transitionSource, stateIdToMatch)

    def _findReachedState(self, parentState: stateMachineModule.State, stateIdToMatch: str) -> stateMachineModule.State | None:
        if parentState.id == stateIdToMatch:
            return parentState

        currentState: stateMachineModule.State | None = parentState.getNestedInitialState()

        while not currentState is parentState and not currentState is None:
            if currentState.id == stateIdToMatch:
                return currentState

            currentState = currentState.parentState

        return None
