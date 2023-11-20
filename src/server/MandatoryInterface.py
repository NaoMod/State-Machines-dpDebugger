from parser.StateMachineLexer import StateMachineLexer
from parser.StateMachineParser import StateMachineParser

from antlr4 import CommonTokenStream, FileStream
from server.LRP import InitializeResponse, LanguageRuntimeCapabilities, ParseResponse
from statemachine_ast.ASTRegistry import ASTRegistry
from statemachine_ast.BuildASTVisitor import BuildASTVisitor
from statemachine_ast.StateMachine import StateMachine


class MandatoryInterface:
    """Exposes the mandatory services for any language server.

    Attributes:
        registry (ASTRegistry): registry of ASTs.
    """

    def __init__(self, registry: ASTRegistry) -> None:
        self.registry: ASTRegistry = registry

    def initialize(self) -> InitializeResponse:
        capabilities: LanguageRuntimeCapabilities = LanguageRuntimeCapabilities(
            False, False, False
        )
        return InitializeResponse(capabilities)

    def parse(self, file: str) -> ParseResponse:
        """Parses a file and stores the generated StateMachine in self.registry.

        Args:
            file (str): URI of the file to parse.
        """

        text_input = FileStream(file)
        lexer = StateMachineLexer(text_input)
        stream = CommonTokenStream(lexer)
        parser = StateMachineParser(stream)
        tree = parser.statemachine()

        visitor = BuildASTVisitor()
        state_machine: StateMachine = visitor.visitStatemachine(tree)
        self.registry.set_ast(file, state_machine)

        return ParseResponse(state_machine)
