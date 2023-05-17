from parser.StateMachineParser import StateMachineParser
from parser.StateMachineVisitor import StateMachineVisitor

from antlr4 import Token
from server.LRP import Location

from .StateMachine import (CompositeState, InitialState, SimpleState, State,
                           StateMachine)


class StateRegistry:
    """Registry of created states.

    Attributes:
        simple_states (dict[str, SimpleState]): map of names to their related simple state.
        composite_states (dict[str, CompositeState]): map of names to their related composite state.
    """

    def __init__(self) -> None:
        self.simple_states: dict[str, SimpleState] = {}
        self.composite_states: dict[str, CompositeState] = {}

    def get(self, name: str) -> State | None:
        if self.simple_states.get(name) is not None:
            return self.simple_states[name]

        return self.composite_states.get(name)


class BuildASTVisitor(StateMachineVisitor):
    """Builds an instance of StateMachine from a StatemachineContext.

    Attributes:
        state_registry (StateRegistry): registry of created states.
        current_parent_state (State): parent state of the state currently being created.
    """

    # Visit a parse tree produced by StateMachineParser#statemachine.
    def visitStatemachine(self, ctx: StateMachineParser.StatemachineContext):
        state_machine: StateMachine = StateMachine(ctx.NAME().getText())

        # First pass to create empty states so references can be made easily
        empty_states_visitor: BasicBuildEmptyStatesVisitor = BasicBuildEmptyStatesVisitor()
        self.state_registry: StateRegistry = empty_states_visitor.visitStatemachine(
            ctx)
        state_machine.initial_state = ctx.initial_state().accept(self)

        for state in ctx.states:
            self.current_parent_state: State | None = None
            state_machine.states.append(state.accept(self))

        return state_machine

    def visitInitial_state(self, ctx: StateMachineParser.Initial_stateContext):
        return InitialState(self.state_registry.get(ctx.target.text))

    def visitState_rule(self, ctx: StateMachineParser.State_ruleContext) -> State:
        return ctx.getChild(0).accept(self)

    # Visit a parse tree produced by StateMachineParser#composite_state.
    def visitComposite_state(self, ctx: StateMachineParser.Composite_stateContext) -> CompositeState:
        state: CompositeState = self.state_registry.composite_states[ctx.NAME(
        ).getText()]

        state.initial_state = InitialState(
            self.state_registry.get(ctx.initial_state().target.text))

        self._create_transitions(state, ctx)

        for contained_state in ctx.states:
            self.current_parent_state = state
            state.states.append(contained_state.accept(self))

        return state

    # Visit a parse tree produced by StateMachineParser#simple_state.
    def visitSimple_state(self, ctx: StateMachineParser.Simple_stateContext) -> SimpleState:
        state: SimpleState = self.state_registry.simple_states[ctx.NAME(
        ).getText()]

        self._create_transitions(state, ctx)

        return state

    def _create_transitions(self, state: State, ctx: StateMachineParser.Composite_stateContext | StateMachineParser.Simple_stateContext) -> None:
        state.parent_state = self.current_parent_state

        for transition in ctx.transitions:
            start_token: Token = transition.TRANSITION_SYMBOL().symbol
            end_token: Token = transition.stop
            location: Location = Location(
                start_token.line, end_token.line, start_token.column+1, end_token.column+1)

            if transition.target.text == 'FINAL':
                state.create_transition(SimpleState(
                    parent_state=self.current_parent_state, is_final=True), transition.input_.text.strip("'"), transition.output.text.strip("'"), location)
            else:
                state.create_transition(
                    self.state_registry.get(transition.target.text), transition.input_.text.strip("'"), transition.output.text.strip("'"), location)


class BasicBuildEmptyStatesVisitor(StateMachineVisitor):
    """Builds empty states from a StatemachineContext.

    Attributes:
        state_registry (StateRegistry): registry of created states.
    """

    def visitStatemachine(self, ctx: StateMachineParser.StatemachineContext) -> StateRegistry:
        self.state_registry: StateRegistry = StateRegistry()

        for state in ctx.states:
            state.accept(self)

        return self.state_registry

    def visitState_rule(self, ctx: StateMachineParser.State_ruleContext):
        ctx.getChild(0).accept(self)

    def visitSimple_state(self, ctx: StateMachineParser.Simple_stateContext):
        start_token: Token = ctx.STATE().symbol
        end_token: Token = ctx.NAME().symbol
        location: Location = Location(
            start_token.line, end_token.line, start_token.column+1, end_token.column+1+(end_token.stop-end_token.start))

        if self.state_registry.get(ctx.NAME().getText()) is not None:
            raise DuplicatedNameError(ctx.NAME().getText())

        self.state_registry.simple_states[ctx.NAME().getText()] = SimpleState(
            ctx.NAME().getText(), location=location)

    def visitComposite_state(self, ctx: StateMachineParser.Composite_stateContext):
        start_token: Token = ctx.COMPOSITE_STATE().symbol
        end_token: Token = ctx.NAME().symbol
        location: Location = Location(
            start_token.line, end_token.line, start_token.column+1, end_token.column+1+(end_token.stop-end_token.start))

        if self.state_registry.get(ctx.NAME().getText()) is not None:
            raise DuplicatedNameError(ctx.NAME().getText())

        self.state_registry.composite_states[ctx.NAME().getText()] = CompositeState(
            ctx.NAME().getText(), location)

        for state in ctx.states:
            state.accept(self)


class DuplicatedNameError(ValueError):

    def __init__(self, duplicated_name: str, *args: object) -> None:
        super().__init__(*args)
        self.duplicated_name = duplicated_name

    def __str__(self) -> str:
        return f'State names must be unique. Name \'{self.duplicated_name}\' is duplicated.'
