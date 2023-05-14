from .StateMachine import StateMachine


class ASTRegistry:
    """Stores the AST produced from each source file.

    Attributes:
        loaded_sources (dict[str, StateMachine]): dictionary of source files mapped to their parsed state machine.
    """

    def __init__(self) -> None:
        self.loaded_sources: dict[str, StateMachine] = {}

    def set_ast(self, source_file: str, state_machine: StateMachine) -> None:
        self.loaded_sources[source_file] = state_machine
