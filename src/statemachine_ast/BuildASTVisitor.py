from parser.StateMachineParser import StateMachineParser
from parser.StateMachineVisitor import StateMachineVisitor

from antlr4 import Token
from server.LRP import Location

from .StateMachine import (
    Assignment,
    BinaryExpression,
    CompositeState,
    Expression,
    InitialState,
    NumberAtomicExpression,
    Operand,
    ParenthesizedExpression,
    Sign,
    SimpleState,
    State,
    StateMachine,
    Transition,
    VariableAtomicExpression,
)


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
        empty_states_visitor: BasicBuildEmptyStatesVisitor = (
            BasicBuildEmptyStatesVisitor()
        )
        self.state_registry: StateRegistry = empty_states_visitor.visitStatemachine(ctx)
        state_machine.initial_state = ctx.initial_state().accept(self)

        for state in ctx.states:
            self.current_state_parent: State | None = None
            state_machine.states.append(state.accept(self))

        return state_machine

    def visitInitial_state(self, ctx: StateMachineParser.Initial_stateContext):
        return InitialState(self.state_registry.get(ctx.target.text))

    def visitState_rule(self, ctx: StateMachineParser.State_ruleContext) -> State:
        return ctx.getChild(0).accept(self)

    # Visit a parse tree produced by StateMachineParser#composite_state.
    def visitComposite_state(
        self, ctx: StateMachineParser.Composite_stateContext
    ) -> CompositeState:
        state: CompositeState = self.state_registry.composite_states[
            ctx.NAME().getText()
        ]

        state.initial_state = InitialState(
            self.state_registry.get(ctx.initial_state().target.text)
        )

        self.current_transition_parent = state
        transitions: list[Transition] = [
            transition.accept(self) for transition in ctx.transitions
        ]
        self._assign_transitions_to_states(transitions)

        for contained_state in ctx.states:
            self.current_state_parent = state
            state.states.append(contained_state.accept(self))

        return state

    # Visit a parse tree produced by StateMachineParser#simple_state.
    def visitSimple_state(
        self, ctx: StateMachineParser.Simple_stateContext
    ) -> SimpleState:
        state: SimpleState = self.state_registry.simple_states[ctx.NAME().getText()]
        state.parent_state = self.current_state_parent
        self.current_transition_parent = state

        transitions: list[Transition] = [
            transition.accept(self) for transition in ctx.transitions
        ]
        self._assign_transitions_to_states(transitions)

        return state

    # Visit a transition tree produced by StateMachineParser#transition.
    def visitTransition(self, ctx: StateMachineParser.TransitionContext) -> Transition:
        start_token: Token = ctx.TRANSITION_SYMBOL().symbol
        end_token: Token = ctx.target
        assignments: list[Assignment] = [
            assignment.accept(self) for assignment in ctx.assignments
        ]
        location: Location = Location(
            start_token.line,
            end_token.line,
            start_token.column + 1,
            end_token.column + len(end_token.text),
        )

        step_location: Location = Location(
            start_token.line,
            ctx.stop.line,
            start_token.column + 1,
            ctx.stop.column + len(ctx.stop.text) + 1,
        )

        if ctx.target.text == "FINAL":
            return Transition(
                self.current_transition_parent,
                SimpleState(parent_state=self.current_state_parent, is_final=True),
                ctx.input_.text.strip("'"),
                ctx.output.text.strip("'"),
                assignments,
                location,
                step_location,
            )
        else:
            return Transition(
                self.current_transition_parent,
                self.state_registry.get(ctx.target.text),
                ctx.input_.text.strip("'"),
                ctx.output.text.strip("'"),
                assignments,
                location,
                step_location,
            )

    def visitSeparated_assignment(
        self, ctx: StateMachineParser.Separated_assignmentContext
    ) -> Assignment:
        assignment: Assignment = ctx.assignment().accept(self)
        location: Location = Location(
            ctx.start.line, ctx.stop.line, ctx.start.column + 1, ctx.stop.column + 1
        )
        assignment.location = location
        step_location: Location = Location(
            location.line, location.endLine, location.column, location.endColumn + 1
        )
        assignment.step_location = step_location

        return assignment

    def visitAssignment(self, ctx: StateMachineParser.AssignmentContext) -> Assignment:
        return Assignment(ctx.variable().getText(), ctx.expression().accept(self))

    def visitExpression(self, ctx: StateMachineParser.ExpressionContext) -> Expression:
        if ctx.atom() is not None:
            if ctx.atom().number() is not None:
                return NumberAtomicExpression(
                    float(ctx.atom().getText()), self._find_sign(ctx)
                )
            else:
                return VariableAtomicExpression(
                    ctx.atom().getText(), self._find_sign(ctx)
                )

        if len(ctx.expression()) == 1:
            return ParenthesizedExpression(ctx.expression()[0].accept(self))

        operand: Operand | None = self._find_operand(ctx)
        assert (
            len(ctx.expression()) == 2 and operand is not None
        ), "Malformed expression."
        return BinaryExpression(
            ctx.expression()[0].accept(self), ctx.expression()[1].accept(self), operand
        )

    def _assign_transitions_to_states(self, transitions: list[Transition]) -> None:
        for transition in transitions:
            transition.source.outgoing_transitions.append(transition)
            transition.target.incoming_transitions.append(transition)

    def _find_sign(self, ctx: StateMachineParser.ExpressionContext) -> Sign | None:
        if ctx.PLUS() is not None:
            return Sign.PLUS

        if ctx.MINUS() is not None:
            return Sign.MINUS

        return None

    def _find_operand(
        self, ctx: StateMachineParser.ExpressionContext
    ) -> Operand | None:
        if ctx.PLUS() is not None:
            return Operand.PLUS

        if ctx.MINUS() is not None:
            return Operand.MINUS

        if ctx.TIMES() is not None:
            return Operand.TIMES

        if ctx.DIV() is not None:
            return Operand.DIV

        if ctx.POW() is not None:
            return Operand.POW

        return None


class BasicBuildEmptyStatesVisitor(StateMachineVisitor):
    """Builds empty states from a StatemachineContext.

    Attributes:
        state_registry (StateRegistry): registry of created states.
    """

    def visitStatemachine(
        self, ctx: StateMachineParser.StatemachineContext
    ) -> StateRegistry:
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
            start_token.line,
            end_token.line,
            start_token.column + 1,
            end_token.column + 1 + (end_token.stop - end_token.start),
        )

        if self.state_registry.get(ctx.NAME().getText()) is not None:
            raise DuplicatedNameError(ctx.NAME().getText())

        self.state_registry.simple_states[ctx.NAME().getText()] = SimpleState(
            ctx.NAME().getText(), location=location
        )

    def visitComposite_state(self, ctx: StateMachineParser.Composite_stateContext):
        start_token: Token = ctx.COMPOSITE_STATE().symbol
        end_token: Token = ctx.NAME().symbol
        location: Location = Location(
            start_token.line,
            end_token.line,
            start_token.column + 1,
            end_token.column + 1 + (end_token.stop - end_token.start),
        )

        if self.state_registry.get(ctx.NAME().getText()) is not None:
            raise DuplicatedNameError(ctx.NAME().getText())

        self.state_registry.composite_states[ctx.NAME().getText()] = CompositeState(
            ctx.NAME().getText(), location
        )

        for state in ctx.states:
            state.accept(self)


class DuplicatedNameError(ValueError):
    def __init__(self, duplicated_name: str, *args: object) -> None:
        super().__init__(*args)
        self.duplicated_name = duplicated_name

    def __str__(self) -> str:
        return f"State names must be unique. Name {self.duplicated_name} is duplicated."
