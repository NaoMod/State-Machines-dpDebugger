from .StateMachine import StateMachine


class ASTRegistry:
    """Stores the AST produced from each source file.

    Attributes:
        loadedSources (dict[str, statemachine_ls.statemachine_ast.StateMachine.StateMachine]): dictionary of source files mapped to their parsed state machine.
    """

    def __init__(self) -> None:
        self.loadedSources: dict[str, StateMachine] = {}

    def setAST(self, sourceFile: str, stateMachine: StateMachine) -> None:
        self.loadedSources[sourceFile] = stateMachine
