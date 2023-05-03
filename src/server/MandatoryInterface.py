from parser.StateMachineLexer import StateMachineLexer
from parser.StateMachineParser import StateMachineParser

from antlr4 import CommonTokenStream, FileStream
from statemachine_ast.ASTRegistry import ASTRegistry
from statemachine_ast.BuildASTVisitor import BuildASTVisitor
from statemachine_ast.StateMachine import StateMachine

from server.LRP import ParseResponse


class MandatoryInterface:
    """Exposes the mandatory services for any language server.

    Attributes:
        registry (statemachine_ls.statemachine_ast.ASTRegistry.ASTRegistry): registry of ASTs.
    """

    def __init__(self, registry: ASTRegistry) -> None:
        self.registry: ASTRegistry = registry

    def parse(self, file: str) -> ParseResponse:
        """Parses a file and stores the generated `statemachine_ls.statemachine_ast.StateMachine.StateMachine` in `self.registry`.

        Args:
            file (str): URI of the file to parse.
        """

        textInput = FileStream(file)
        lexer = StateMachineLexer(textInput)
        stream = CommonTokenStream(lexer)
        parser = StateMachineParser(stream)
        tree = parser.statemachine()

        visitor = BuildASTVisitor()
        stateMachine: StateMachine = visitor.visitStatemachine(tree)
        self.registry.setAST(file, stateMachine)

        return ParseResponse(stateMachine)
