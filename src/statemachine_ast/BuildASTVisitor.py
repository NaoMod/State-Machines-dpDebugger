from parser.StateMachineParser import StateMachineParser
from parser.StateMachineVisitor import StateMachineVisitor

from .StateMachine import (CompositeState, InitialState, SimpleState, State,
                           StateMachine, ASTElement)
from server.LRP import Location

from antlr4 import Token

class StateRegistry:
    """Registry of created states.

    Attributes:
        simpleStates (dict[str, statemachine_ls.statemachine_ast.StateMachine.SimpleState]): map of names to their simple state.
        compositeStates (dict[str, statemachine_ls.statemachine_ast.StateMachine.CompositeState]): map of names to their related composite state.
    """    

    def __init__(self) -> None:
        self.simpleStates: dict[str, SimpleState] = {}
        self.compositeStates: dict[str, CompositeState] = {}

    def get(self, name: str) -> State:
        if not self.simpleStates.get(name) is None:
            return self.simpleStates.get(name)

        return self.compositeStates.get(name)


class BuildASTVisitor(StateMachineVisitor):
    """Builds an instance of `statemachine_ls.statemachine_ast.StateMachine.StateMachine` from a `statemachine_ls.parser.StateMachineParser.StateMachineParser.StatemachineContext`.
    
    Attributes:
        stateRegistry (statemachine_ls.statemachine_ast.BuildASTVisitor.StateRegistry): registry of created states.
        currentParentState (statemachine_ls.statemachine_ast.StateMachine.State): parent state of the state currently being created. 
    """

    # Visit a parse tree produced by StateMachineParser#statemachine.
    def visitStatemachine(self, ctx: StateMachineParser.StatemachineContext):
        stateMachine: StateMachine = StateMachine(ctx.NAME().getText())

        # First pass to create empty states so references can be made easily
        emptyStatesVisitor: BasicBuildEmptyStatesVisitor = BasicBuildEmptyStatesVisitor()
        self.stateRegistry: StateRegistry = emptyStatesVisitor.visitStatemachine(
            ctx)
        stateMachine.initialState = ctx.initial_state().accept(self)

        for state in ctx.states:
            self.currentParentState: State = None
            stateMachine.states.append(state.accept(self))

        return stateMachine

    def visitInitial_state(self, ctx: StateMachineParser.Initial_stateContext):
        return InitialState(self.stateRegistry.get(ctx.target.text))

    def visitState_rule(self, ctx: StateMachineParser.State_ruleContext) -> State:
        return ctx.getChild(0).accept(self)

    # Visit a parse tree produced by StateMachineParser#composite_state.
    def visitComposite_state(self, ctx: StateMachineParser.Composite_stateContext) -> CompositeState:
        state: CompositeState = self.stateRegistry.compositeStates.get(
            ctx.NAME().getText())

        state.initialState = InitialState(
            self.stateRegistry.get(ctx.initial_state().target.text))
        state.parentState = self.currentParentState

        for transition in ctx.transitions:
            startToken: Token = transition.TRANSITION_SYMBOL().symbol
            endToken: Token = transition.stop
            location: Location = Location(startToken.line, endToken.line, startToken.column+1, endToken.column+1)

            if transition.target.text == 'FINAL':
                state.createTransition(SimpleState(
                    parentState=self.currentParentState, isFinal=True), transition.input_.text.strip("'"), transition.output.text.strip("'"), location)
            else:
                state.createTransition(
                    self.stateRegistry.get(transition.target.text), transition.input_.text.strip("'"), transition.output.text.strip("'"), location)

        for containedState in ctx.states:
            self.currentParentState: State = state
            state.states.append(containedState.accept(self))

        return state

    # Visit a parse tree produced by StateMachineParser#simple_state.
    def visitSimple_state(self, ctx: StateMachineParser.Simple_stateContext) -> SimpleState:
        state: SimpleState = self.stateRegistry.simpleStates.get(
            ctx.NAME().getText())
        state.parentState = self.currentParentState

        for transition in ctx.transitions:
            startToken: Token = transition.TRANSITION_SYMBOL().symbol
            endToken: Token = transition.stop
            location: Location = Location(startToken.line, endToken.line, startToken.column+1, endToken.column+1)

            if transition.target.text == 'FINAL':
                state.createTransition(SimpleState(
                    parentState=self.currentParentState, isFinal=True), transition.input_.text.strip("'"), transition.output.text.strip("'"), location)
            else:
                state.createTransition(
                    self.stateRegistry.get(transition.target.text), transition.input_.text.strip("'"), transition.output.text.strip("'"), location)

        return state


class BasicBuildEmptyStatesVisitor(StateMachineVisitor):
    """Builds empty states from a `statemachine_ls.parser.StateMachineParser.StateMachineParser.StatemachineContext`.

    Attributes:
        stateRegistry (statemachine_ls.statemachine_ast.BuildASTVisitor.StateRegistry): registry of created states.
    """    

    def visitStatemachine(self, ctx: StateMachineParser.StatemachineContext) -> StateRegistry:
        self.stateRegistry: StateRegistry = StateRegistry()

        for state in ctx.states:
            state.accept(self)

        return self.stateRegistry

    def visitState_rule(self, ctx: StateMachineParser.State_ruleContext):
        ctx.getChild(0).accept(self)

    def visitSimple_state(self, ctx: StateMachineParser.Simple_stateContext):
        startToken: Token = ctx.STATE().symbol
        endToken: Token = ctx.NAME().symbol
        location: Location = Location(startToken.line, endToken.line, startToken.column+1, endToken.column+1)

        if not self.stateRegistry.get(ctx.NAME().getText()) is None:
            raise Exception('State names must be unique. Name ' +
                            ctx.NAME().getText() + ' is duplicated.')

        self.stateRegistry.simpleStates[ctx.NAME().getText()] = SimpleState(
            ctx.NAME().getText(), location=location)

    def visitComposite_state(self, ctx: StateMachineParser.Composite_stateContext):
        startToken: Token = ctx.COMPOSITE_STATE().symbol
        endToken: Token = ctx.NAME().symbol
        location: Location = Location(startToken.line, endToken.line, startToken.column+1, endToken.column+1)

        if not self.stateRegistry.get(ctx.NAME().getText()) is None:
            raise Exception('State names must be unique. Name ' +
                            ctx.NAME().getText() + ' is duplicated.')

        self.stateRegistry.compositeStates[ctx.NAME().getText()] = CompositeState(
            ctx.NAME().getText(), location)

        for state in ctx.states:
            state.accept(self)
