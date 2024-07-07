from bsonrpc import request, service_class
from server.ServiceHandler import ServiceHandler

from .DictBuilder import (
    from_check_breakpoint_response,
    from_enter_composite_step_response,
    from_execute_atomic_step_response,
    from_get_available_steps_response,
    from_get_breakpoint_types_response,
    from_get_runtime_state_response,
    from_get_step_location_response,
    from_initialize_execution_response,
    from_parse_response,
)
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
        return from_parse_response(
            self.service_handler.parse(ParseArguments(args["sourceFile"]))
        )

    @request
    def initializeExecution(self, args: dict) -> dict:
        return from_initialize_execution_response(
            self.service_handler.initialize_execution(
                InitializeExecutionArguments(args["sourceFile"], args["entries"])
            )
        )

    @request
    def getRuntimeState(self, args: dict) -> dict:
        return from_get_runtime_state_response(
            self.service_handler.get_runtime_state(
                GetRuntimeStateArguments(args["sourceFile"])
            )
        )

    @request
    def getBreakpointTypes(self) -> dict:
        return from_get_breakpoint_types_response(
            self.service_handler.get_breakpoint_types()
        )

    @request
    def checkBreakpoint(self, args: dict) -> dict:
        return from_check_breakpoint_response(
            self.service_handler.check_breakpoint(
                CheckBreakpointArguments(
                    args["sourceFile"],
                    args["typeId"],
                    args["stepId"],
                    args["entries"],
                )
            )
        )

    @request
    def getAvailableSteps(self, args: dict) -> dict:
        return from_get_available_steps_response(
            self.service_handler.get_available_steps(
                GetAvailableStepsArguments(args["sourceFile"])
            )
        )

    @request
    def enterCompositeStep(self, args: dict) -> dict:
        return from_enter_composite_step_response(
            self.service_handler.enter_composite_step(
                EnterCompositeStepArguments(args["sourceFile"], args["stepId"])
            )
        )

    @request
    def executeAtomicStep(self, args: dict) -> dict:
        return from_execute_atomic_step_response(
            self.service_handler.execute_atomic_step(
                ExecuteAtomicStepArguments(args["sourceFile"], args["stepId"])
            )
        )

    @request
    def getStepLocation(self, args: dict) -> dict:
        return from_get_step_location_response(
            self.service_handler.get_step_location(
                GetStepLocationArguments(args["sourceFile"], args["stepId"])
            )
        )
