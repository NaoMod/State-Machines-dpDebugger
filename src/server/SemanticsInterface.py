from __future__ import annotations

import statemachine_ast.ASTRegistry as astRegistryModule
from server.ExposedTypes import breakpoints, steppingModes
from server.LRP import (
    CheckBreakpointArguments,
    CheckBreakpointResponse,
    GetAvailableStepsArguments,
    GetAvailableStepsResponse,
    GetBreakpointTypesResponse,
    GetRuntimeStateResponse,
    GetStepLocationArguments,
    GetStepLocationResponse,
    GetSteppingModesResponse,
    InitArguments,
    InitResponse,
    Location,
    StepArguments,
    StepResponse,
)
from server.Runtime import Runtime, RuntimeState


class SemanticsInterface:
    """Exposes the services related to execution semantics.

    Attributes:
        runtimes (dict[str, Runtime]): map of source files to their runtime
        registry (ASTRegistry): registry of all already parsed ASTs.
    """

    def __init__(self, registry: astRegistryModule.ASTRegistry) -> None:
        self.runtimes: dict[str, Runtime] = {}
        self.registry: astRegistryModule.ASTRegistry = registry

    def init_execution(self, args: InitArguments) -> InitResponse:
        """Creates a new runtime for a given source file.
        The AST for the given source file must have been previously constructed.

        Args:
            args (InitArguments): arguments required to start an execution.

        Returns:
            InitResponse: response with the result of the initialization.
        """

        self.runtimes[args.source_file] = Runtime(
            self.registry.loaded_sources[args.source_file], args.inputs
        )

        next_transition = self.runtimes[args.source_file].find_next_transition()

        return InitResponse(next_transition is None)

    def get_breakpoint_types(self) -> GetBreakpointTypesResponse:
        return GetBreakpointTypesResponse(breakpoints)

    def execute_step(self, args: StepArguments) -> StepResponse:
        """Performs a next step action in the runtime associated to a given source file.

        Args:
            source_file (str): source file for which to initialize the execution.

        Returns:
            StepResponse: response with the result of the performed step.
        """

        self._check_runtime_exists(args.sourceFile)
        executed_step = self.runtimes[args.sourceFile].execute_step(args.stepId)

        return StepResponse(
            [x.id for x in executed_step.get_completed_steps()],
            self.runtimes[args.sourceFile].find_next_transition() is None,
        )

    def get_runtime_state(self, source_file: str) -> GetRuntimeStateResponse:
        """Returns the current runtime state for a given source file.

        Args:
            source_file (str): source file for which to return the runtime state

        Raises:
            ExecutionAlreadyDoneError: raised if the execution is done.

        Returns:
            RuntimeState: current runtime state for the source file.
        """

        self._check_runtime_exists(source_file)

        return GetRuntimeStateResponse(RuntimeState(self.runtimes[source_file]))

    def check_breakpoint(
        self, args: CheckBreakpointArguments
    ) -> CheckBreakpointResponse:
        """Checks whether a breakpoint is activated.

        Args:
            args (CheckBreakpointArgs): arguments required to check a breakpoint.

        Returns:
            CheckBreakpointResponse: response with the result of the breakpoint checking.
        """
        self._check_runtime_exists(args.sourceFile)

        return self.runtimes[args.sourceFile].check_breakpoint(
            args.typeId, args.elementId, args.stepId
        )

    def get_stepping_modes(self) -> GetSteppingModesResponse:
        return GetSteppingModesResponse(steppingModes)

    def get_available_steps(
        self, args: GetAvailableStepsArguments
    ) -> GetAvailableStepsResponse:
        self._check_runtime_exists(args.sourceFile)

        runtime = self.runtimes[args.sourceFile]
        available_steps = list(
            runtime.compute_available_steps(args.compositeStepId).values()
        )
        parent_step = (
            available_steps[0].parent_step if len(available_steps) > 0 else None
        )

        return GetAvailableStepsResponse(
            [step.to_LRP_step() for step in available_steps],
            parent_step.id if parent_step is not None else None,
        )

    def get_step_location(
        self, args: GetStepLocationArguments
    ) -> GetStepLocationResponse:
        self._check_runtime_exists(args.sourceFile)
        step = self.runtimes[args.sourceFile].available_steps.get(args.stepId)
        assert step is not None, f"No step with id {args.stepId}."
        location: Location | None = (
            None
            if step.location is None
            else Location(
                step.location.line,
                step.location.endLine,
                step.location.column,
                step.location.endColumn + 1,
            )
        )

        return GetStepLocationResponse(location)

    def _check_runtime_exists(self, source_file: str) -> None:
        """Checks that a runtime exists for a given source file.

        Args:
            source_file (str): source file for which to search for a runtime.

        Raises:
            ValueError: raised if no runtime is found.
        """

        if self.runtimes[source_file] is None:
            raise ValueError(f"No runtime for source file {source_file}.")
