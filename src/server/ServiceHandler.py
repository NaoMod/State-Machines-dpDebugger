from pathlib import Path

from bsonrpc import request, service_class
from statemachine_ast.ASTRegistry import ASTRegistry

from .LRP import CheckBreakpointArgs
from .MandatoryInterface import MandatoryInterface
from .SemanticsInterface import InitArguments, SemanticsInterface


@service_class
class ServiceHandler:
    """Facade for the services exposed by the language server.
    These services are called by the JSON-RPC handler.

    Attributes:
        registry (ASTRegistry): registry of all ASTs.
        mandatory_interface (MandatoryInterface): interface for mandatory services.
        semantics_interface (SemanticsInterface): interface for execution semantics services.
    """

    def __init__(self) -> None:
        self.registry: ASTRegistry = ASTRegistry()
        self.mandatory_interface: MandatoryInterface = MandatoryInterface(
            self.registry)
        self.semantics_interface: SemanticsInterface = SemanticsInterface(
            self.registry)

    @request
    def parse(self, args: dict) -> dict:
        return self.mandatory_interface.parse(args['sourceFile']).to_dict()

    @request
    def initExecution(self, args: dict) -> dict:
        return self.semantics_interface.init_execution(
            InitArguments(args['sourceFile'], args['inputs'])).to_dict()

    @request
    def getBreakpointTypes(self) -> dict:
        return self.semantics_interface.get_breakpoint_types().to_dict()

    @request
    def nextStep(self, args: dict) -> dict:
        return self.semantics_interface.next_step(args['sourceFile']).to_dict()

    @request
    def getRuntimeState(self, args: dict) -> dict:
        return self.semantics_interface.get_runtime_state(args['sourceFile']).to_dict()

    @request
    def checkBreakpoint(self, args: dict) -> dict:
        return self.semantics_interface.check_breakpoint(CheckBreakpointArgs(args['sourceFile'], args['typeId'], args['elementId'])).to_dict()
