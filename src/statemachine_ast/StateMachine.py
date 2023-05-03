from __future__ import annotations

from abc import abstractmethod

from server.LRP import ASTElement, Location


class StateMachine(ASTElement):
    """Represents a state machine.

    Attributes:
        name (str): name of the state machine.
        initialState (statemachine_ls.statemachine_ast.StateMachine.InitialState): initial state of the state machine.
        states (list[statemachine_ls.statemachine_ast.StateMachine.State]): list of the states directly contained in the state machine.
    """

    def __init__(self, name: str, location: Location | None = None) -> None:
        super().__init__('stateMachine.stateMachine', location)
        self.name = name
        self.initialState: InitialState | None = None
        self.states: list[State] = []

    def toDict(self) -> dict:
        return super().constructDict(
            {'name': self.name},
            {'states': list(map(lambda state: state.toDict(), self.states))},
            {'initialState': '' if self.initialState is None else self.initialState.target.id, }
        )


class State(ASTElement):
    """Abstract class for a state.

    Attributes:
        name (str): name of the state.
        parentState (statemachine_ls.statemachine_ast.StateMachine.State): composite state containing the current state. For states at the top-level, this attribute is None.
        isFinal (bool): True if the state is final, False otherwise.
        outgoingTransitions (list[statemachine_ls.statemachine_ast.StateMachine.Transition]): list of transitions going out of the state.
        incomingTransitions (list[statemachine_ls.statemachine_ast.StateMachine.Transition]): list of transitions coming in the state.s
    """

    def __init__(self, name: str | None = None, parentState: State | None = None, isFinal: bool = False, location: Location | None = None):
        super().__init__('stateMachine.state', location)
        self.name: str | None = name
        self.parentState: State | None = parentState
        self.isFinal = isFinal
        self.outgoingTransitions: list[Transition] = []
        self.incomingTransitions: list[Transition] = []
        self.states = []

    def addTransitions(self, transitions: list[Transition]) -> None:
        for transition in transitions:
            self.outgoingTransitions.append(transition)

        for transition in transitions:
            transition.target.incomingTransitions.append(transition)

    def createTransition(self, target: State, input: str | None = None, output: str | None = None, location: Location | None = None) -> None:
        transition: Transition = Transition(
            self, target, input, output, location)
        self.outgoingTransitions.append(transition)
        target.incomingTransitions.append(transition)

    @abstractmethod
    def getNestedInitialState(self) -> State:
        return self

    def getDepth(self) -> int:
        if self.parentState is None:
            return 0
        else:
            return self.parentState.getDepth()+1

    def constructDict(self, attributes: dict, children: dict, refs: dict) -> dict:
        transitions: list[Transition] = list(filter(
            lambda transition: not transition.target.isFinal, self.outgoingTransitions))
        finalTransitions: list[Transition] = list(
            filter(lambda transition: transition.target.isFinal, self.outgoingTransitions))

        return super().constructDict(
            {
                'name': self.name,
                **attributes
            },
            {
                'transitions': list(map(lambda transition: transition.toDict(), transitions)),
                'final transitions': list(map(lambda transition: transition.toDict(), finalTransitions)),
                **children
            },
            {**refs}
        )


class SimpleState(State):
    """State that contains no other states.
    """

    def __init__(self, name: str | None = None, parentState: State | None = None, isFinal: bool = False, location: Location | None = None):
        super().__init__(name, parentState, isFinal, location)

    def getNestedInitialState(self) -> State:
        return super().getNestedInitialState()

    def toDict(self) -> dict:
        return super().constructDict(
            {},
            {},
            {}
        )


class CompositeState(State):
    """State that can contain other states.

    Attributes:
        states (list[statemachine_ls.statemachine_ast.StateMachine.State]): list of the states directly contained in the state machine.
        initialState (statemachine_ls.statemachine_ast.StateMachine.InitialState): initial state of the state machine.
    """

    def __init__(self,  name: str, location: Location | None = None):
        super().__init__(name, None, False, location)
        self.initialState = None

    def getNestedInitialState(self) -> State:
        if self.initialState is None:
            raise ValueError('No initial state.')

        return self.initialState.getNestedInitialState()

    def toDict(self) -> dict:
        if self.initialState is None:
            raise ValueError('No initial state.')

        return super().constructDict(
            {},
            {'states': list(map(lambda state: state.toDict(), self.states))},
            {'initialState': self.initialState.target.id}
        )


class InitialState:
    """Initial pseudo state.

    Attributes:
        target (statemachine_ls.statemachine_ast.StateMachine.State): target state of the outgoing transition from the initial pseudo state.
        parentState (statemachine_ls.statemachine_ast.StateMachine.State): composite state containing the initial pseudo state. For initial states at the top-level, this attribute is None.
    """

    def __init__(self, target: State) -> None:
        self.target = target
        self.parentState = target.parentState

    def getNestedInitialState(self) -> State:
        return self.target.getNestedInitialState()


class Transition(ASTElement):
    """Represents a transition between two states.

    Attributes:
        source (statemachine_ls.statemachine_ast.StateMachine.State): source state of the transition.
        target (statemachine_ls.statemachine_ast.StateMachine.State): target state of the transition.
        input (str): input required to fire the transition.
    """

    def __init__(self, source: State, target: State, input: str | None = None, output: str | None = None, location: Location | None = None):
        super().__init__('stateMachine.transition', location)
        self.source = source
        self.target = target
        self.input = input
        self.output = output

    def toDict(self) -> dict:
        refs: dict = {}

        if not self.target.isFinal:
            refs['target'] = self.target.id

        return super().constructDict(
            {
                'input': self.input,
                'ouptut': self.output
            },
            {},
            {**refs}
        )
