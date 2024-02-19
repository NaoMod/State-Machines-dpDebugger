from bsonrpc import request, service_class
from server.ServiceHandler import ServiceHandler

from .LRP import (
    CheckBreakpointArguments,
    EnterCompositeStepArguments,
    ExecuteAtomicStepArguments,
    GetAvailableStepsArguments,
    GetRuntimeStateArguments,
    GetStepLocationArguments,
    InitializeExecutionArguments,
    ParseArguments,
)


@service_class
class ServerFacade:
    """Facade for the services exposed by the language server.
    These services are called by the JSON-RPC handler.

    Attributes:
        service_handler (ServiceHandler): object handling LRP services.
    """

    def __init__(self) -> None:
        self.service_handler: ServiceHandler = ServiceHandler()

    @request
    def parse(self, args: dict) -> dict:
        return self.service_handler.parse(ParseArguments(args["sourceFile"])).to_dict()

    @request
    def initializeExecution(self, args: dict) -> dict:
        return self.service_handler.initialize_execution(
            InitializeExecutionArguments(args["sourceFile"], args["bindings"])
        ).to_dict()

    @request
    def getRuntimeState(self, args: dict) -> dict:
        return self.service_handler.get_runtime_state(
            GetRuntimeStateArguments(args["sourceFile"])
        ).to_dict()

    @request
    def getBreakpointTypes(self) -> dict:
        return self.service_handler.get_breakpoint_types().to_dict()

    @request
    def checkBreakpoint(self, args: dict) -> dict:
        return self.service_handler.check_breakpoint(
            CheckBreakpointArguments(
                args["sourceFile"],
                args["typeId"],
                args["stepId"],
                args["bindings"],
            )
        ).to_dict()

    @request
    def getAvailableSteps(self, args: dict) -> dict:
        return self.service_handler.get_available_steps(
            GetAvailableStepsArguments(args["sourceFile"])
        ).to_dict()

    @request
    def enterCompositeStep(self, args: dict) -> dict:
        return self.service_handler.enter_composite_step(
            EnterCompositeStepArguments(args["sourceFile"], args["stepId"])
        ).to_dict()

    @request
    def executeAtomicStep(self, args: dict) -> dict:
        return self.service_handler.execute_atomic_step(
            ExecuteAtomicStepArguments(args["sourceFile"], args["stepId"])
        ).to_dict()

    @request
    def getStepLocation(self, args: dict) -> dict:
        return self.service_handler.get_step_location(
            GetStepLocationArguments(args["sourceFile"], args["stepId"])
        ).to_dict()
