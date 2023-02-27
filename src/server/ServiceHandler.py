from bsonrpc import request, service_class
from statemachine_ast.ASTRegistry import ASTRegistry

from .MandatoryInterface import MandatoryInterface
from .SemanticsInterface import InitArguments, SemanticsInterface
from .LRP import CheckBreakpointArgs


@service_class
class ServiceHandler:
    """Facade for the services exposed by the language server.
    These services are called by the JSON-RPC handler.

    Attributes:
        registry (statemachine_ls.statemachine_ast.ASTRegistry.ASTRegistry): Registry of all ASTs.
        mandatoryInterface (statemachine_ls.server.MandatoryInterface.MandatoryInterface): Interface for mandatory services.
        semanticsInterface (statemachine_ls.server.SemanticsInterface.SemanticsInterface): Interface for execution semantics services.
    """

    def __init__(self) -> None:
        self.registry: ASTRegistry = ASTRegistry()
        self.mandatoryInterface: MandatoryInterface = MandatoryInterface(
            self.registry)
        self.semanticsInterface: SemanticsInterface = SemanticsInterface(
            self.registry)

    @request
    def parse(self, args: dict) -> dict:
        return self.mandatoryInterface.parse(args['sourceFile']).toDict()

    @request
    def initExecution(self, args: dict) -> dict:
        return self.semanticsInterface.initExecution(
            InitArguments(args['sourceFile'], args['inputs'])).toDict()

    @request
    def getBreakpointTypes(self) -> dict:
        return self.semanticsInterface.getBreakpointTypes().toDict()

    @request
    def nextStep(self, args: dict) -> dict:
        return self.semanticsInterface.nextStep(args['sourceFile']).toDict()

    @request
    def getRuntimeState(self, args: dict) -> dict:
        return self.semanticsInterface.getRuntimeState(args['sourceFile']).toDict()

    @request
    def checkBreakpoint(self, args: dict) -> dict:
        return self.semanticsInterface.checkBreakpoint(CheckBreakpointArgs(args['sourceFile'], args['typeId'], args['elementId'])).toDict()
