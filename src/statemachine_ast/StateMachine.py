from __future__ import annotations

from abc import abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import Any

from antlr4 import ParserRuleContext
from server.LRP import Location, ModelElement
from server.Runtime import ExpressionEvaluator
from server.Utils import generate_uuid


@dataclass
class ASTElement:
    types: list[str]
    id: str = field(default_factory=generate_uuid)
    location: Location | None = None
    parser_ctx: ParserRuleContext | None = None

    @abstractmethod
    def to_model_element(self) -> ModelElement:
        pass


class StateMachine(ASTElement):
    """Represents a state machine.

    Attributes:
        name (str): name of the state machine.
        initial_state (InitialState): initial state of the state machine.
        states (list[State]): list of the states directly contained in the state machine.
    """

    def __init__(
        self,
        name: str,
        location: Location | None = None,
        parser_ctx: ParserRuleContext | None = None,
    ) -> None:
        super().__init__(["StateMachine"], location=location, parser_ctx=parser_ctx)
        self.name = name
        self.initial_state: InitialState | None = None
        self.states: list[State] = []

    def to_model_element(self) -> ModelElement:
        return to_model_element(
            self,
            {"name": self.name},
            {"states": [state.to_model_element() for state in self.states]},
            {
                "initialState": ""
                if self.initial_state is None
                else self.initial_state.target.id,
            },
        )


class State(ASTElement):
    """Abstract class for a state.

    Attributes:
        name (str): name of the state.
        parent_state (State): composite state containing the current state. For states at the top-level, this attribute is None.
        is_final (bool): True if the state is final, False otherwise.
        outgoing_transitions (list[Transition]): list of transitions going out of the state.
        incoming_transitions (list[Transition]): list of transitions coming in the state.
        states (list[State]): list of the states directly contained by the state.
    """

    def __init__(
        self,
        name: str | None = None,
        parent_state: State | None = None,
        is_final: bool = False,
        location: Location | None = None,
        additional_types: list[str] | None = None,
        parser_ctx: ParserRuleContext | None = None,
    ):
        types = ["State"]
        if additional_types is not None:
            types.extend(additional_types)
        super().__init__(types, location=location, parser_ctx=parser_ctx)

        self.name: str | None = name
        self.parent_state: State | None = parent_state
        self.is_final = is_final
        self.outgoing_transitions: list[Transition] = []
        self.incoming_transitions: list[Transition] = []
        self.states: list[State] = []

    @abstractmethod
    def get_nested_initial_state(self) -> State:
        return self

    def get_depth(self) -> int:
        if self.parent_state is None:
            return 0
        else:
            return self.parent_state.get_depth() + 1

    def to_model_element(
        self,
        attributes: dict[str, Any],
        children: dict[str, ModelElement],
        refs: dict[str, str],
    ) -> ModelElement:
        transitions: list[Transition] = list(
            filter(
                lambda transition: not transition.target.is_final,
                self.outgoing_transitions,
            )
        )
        final_transitions: list[Transition] = list(
            filter(
                lambda transition: transition.target.is_final, self.outgoing_transitions
            )
        )

        return to_model_element(
            self,
            {"name": self.name, **attributes},
            {
                "transitions": [t.to_model_element() for t in transitions],
                "final transitions": [t.to_model_element() for t in final_transitions],
                **children,
            },
            {**refs},
        )


class SimpleState(State):
    """State that contains no other states."""

    def __init__(
        self,
        name: str | None = None,
        parent_state: State | None = None,
        is_final: bool = False,
        location: Location | None = None,
        parser_ctx: ParserRuleContext | None = None,
    ):
        super().__init__(
            name, parent_state, is_final, location, ["SimpleState"], parser_ctx
        )

    def get_nested_initial_state(self) -> State:
        return super().get_nested_initial_state()

    def to_model_element(self) -> ModelElement:
        return super().to_model_element({}, {}, {})


class CompositeState(State):
    """State that can contain other states.

    Attributes:
        initial_state (InitialState): initial state of the composite state.
    """

    def __init__(
        self,
        name: str,
        location: Location | None = None,
        parser_ctx: ParserRuleContext | None = None,
    ):
        super().__init__(name, None, False, location, ["CompositeState"], parser_ctx)
        self.initial_state: InitialState | None = None

    def get_nested_initial_state(self) -> State:
        if self.initial_state is None:
            raise ValueError("No initial state.")

        return self.initial_state.get_nested_initial_state()

    def to_model_element(self) -> ModelElement:
        if self.initial_state is None:
            raise ValueError("No initial state.")

        return super().to_model_element(
            {},
            {"states": [state.to_model_element() for state in self.states]},
            {"initialState": self.initial_state.target.id},
        )


class InitialState:
    """Initial pseudo state.

    Attributes:
        target (State): target state of the outgoing transition from the initial pseudo state.
        parent_state (State): composite state containing the initial pseudo state. For initial states at the top-level, this attribute is None.
    """

    def __init__(self, target: State) -> None:
        self.target = target
        self.parent_state = target.parent_state

    def get_nested_initial_state(self) -> State:
        return self.target.get_nested_initial_state()


class Transition(ASTElement):
    """Represents a transition between two states.

    Attributes:
        source (State): source state of the transition.
        target (State): target state of the transition.
        trigger (str): event required to fire the transition.
    """

    def __init__(
        self,
        source: State,
        target: State,
        trigger: str | None = None,
        assignments: list[Assignment] | None = None,
        location: Location | None = None,
        parser_ctx: ParserRuleContext | None = None,
    ):
        super().__init__(["Transition"], location=location, parser_ctx=parser_ctx)
        self.source = source
        self.target = target
        self.trigger = trigger
        self.assignments = assignments

    def to_model_element(self) -> ModelElement:
        refs: dict = {}

        if not self.target.is_final:
            refs["target"] = self.target.id

        children = {}

        if len(self.assignments) > 0:
            children["assignments"] = [a.to_model_element() for a in self.assignments]

        return to_model_element(
            self,
            {"trigger": self.trigger},
            {**children},
            {**refs},
        )


class Assignment(ASTElement):
    def __init__(
        self,
        variable: str,
        expression: Expression,
        location: Location | None = None,
        parser_ctx: ParserRuleContext | None = None,
    ):
        super().__init__(["Assignment"], location=location, parser_ctx=parser_ctx)
        self.variable = variable
        self.expression = expression

    def to_model_element(self) -> ModelElement:
        return to_model_element(
            self, {"variable": self.variable, "value": self.expression.value()}, {}, {}
        )


class Expression:
    @abstractmethod
    def value(self) -> str:
        pass

    @abstractmethod
    def accept(self, evaluator: ExpressionEvaluator) -> float:
        pass


@dataclass
class BinaryExpression(Expression):
    left: Expression
    right: Expression
    operand: Operand

    def value(self) -> str:
        return f"{self.left.value()} {self.operand.value} {self.right.value()}"

    def accept(self, evaluator: ExpressionEvaluator) -> float:
        return evaluator.evaluate_binary_expression(self)


@dataclass
class ParenthesizedExpression(Expression):
    contained_expression: Expression
    sign: Sign | None = None

    def value(self) -> str:
        sign_value: str = "" if self.sign is None else self.sign
        return f"{sign_value}({self.contained_expression.value()})"

    def accept(self, evaluator: ExpressionEvaluator) -> float:
        return evaluator.evaluate_parenthesized_expression(self)


@dataclass
class NumberAtomicExpression(Expression):
    number: float
    sign: Sign | None = None

    def value(self) -> str:
        sign_value: str = "" if self.sign is None else self.sign
        return f"{sign_value}{self.number}"

    def accept(self, evaluator: ExpressionEvaluator) -> float:
        return evaluator.evaluate_number_atomic_expression(self)


@dataclass
class VariableAtomicExpression(Expression):
    variable: str
    sign: Sign | None = None

    def value(self) -> str:
        sign_value: str = "" if self.sign is None else self.sign
        return f"{sign_value}{self.variable}"

    def accept(self, evaluator: ExpressionEvaluator) -> float:
        return evaluator.evaluate_variable_atomic_expression(self)


class Operand(Enum):
    POW = "^"
    TIMES = "*"
    DIV = "/"
    PLUS = "+"
    MINUS = "-"


class Sign(Enum):
    PLUS = "+"
    MINUS = "-"


def to_model_element(
    element: ASTElement,
    attributes: dict[str, Any],
    children: dict[str, ModelElement],
    refs: dict[str, str],
) -> ModelElement:
    return ModelElement(
        element.id, element.types, attributes, children, refs, element.location
    )
