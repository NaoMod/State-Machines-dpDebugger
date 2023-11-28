from bsonrpc import request, service_class
from statemachine_ast.ASTRegistry import ASTRegistry

from .LRP import (
    CheckBreakpointArguments,
    GetAvailableStepsArguments,
    GetStepLocationArguments,
    StepArguments,
)
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
        self.mandatory_interface: MandatoryInterface = MandatoryInterface(self.registry)
        self.semantics_interface: SemanticsInterface = SemanticsInterface(self.registry)

    @request
    def parse(self, args: dict) -> dict:
        return self.mandatory_interface.parse(args["sourceFile"]).to_dict()

    @request
    def initExecution(self, args: dict) -> dict:
        return self.semantics_interface.init_execution(
            InitArguments(args["sourceFile"], args["inputs"])
        ).to_dict()

    @request
    def getBreakpointTypes(self) -> dict:
        return self.semantics_interface.get_breakpoint_types().to_dict()

    @request
    def executeStep(self, args: dict) -> dict:
        return self.semantics_interface.execute_step(
            StepArguments(args["sourceFile"], args.get("stepId"))
        ).to_dict()

    @request
    def getRuntimeState(self, args: dict) -> dict:
        return self.semantics_interface.get_runtime_state(args["sourceFile"]).to_dict()

    @request
    def checkBreakpoint(self, args: dict) -> dict:
        return self.semantics_interface.check_breakpoint(
            CheckBreakpointArguments(
                args["sourceFile"],
                args["typeId"],
                args["elementId"],
                args.get("stepId"),
            )
        ).to_dict()

    @request
    def getSteppingModes(self) -> dict:
        return self.semantics_interface.get_stepping_modes().to_dict()

    @request
    def getAvailableSteps(self, args: dict) -> dict:
        return self.semantics_interface.get_available_steps(
            GetAvailableStepsArguments(
                args["sourceFile"], args["steppingModeId"], args.get("compositeStepId")
            )
        ).to_dict()

    @request
    def getStepLocation(self, args: dict) -> dict:
        return self.semantics_interface.get_step_location(
            GetStepLocationArguments(args["sourceFile"], args["stepId"])
        ).to_dict()
