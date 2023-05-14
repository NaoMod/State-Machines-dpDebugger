from __future__ import annotations

import statemachine_ast.ASTRegistry as astRegistryModule

from server.LRP import (BreakpointParameter, BreakpointType,
                        CheckBreakpointArgs, CheckBreakpointResponse,
                        GetBreakpointTypesResponse, GetRuntimeStateResponse,
                        InitArguments, InitResponse, RuntimeState,
                        StepResponse)
from server.Runtime import Runtime
from server.ServerExceptions import ExecutionAlreadyDoneError

breakpoints = [
    BreakpointType('stateMachine.stateReached',
                   'State Reached',
                   [BreakpointParameter(
                       'targetElementType', objectType='stateMachine.state')],
                   'Breaks when a specific state is about to be reached.'),

    BreakpointType('stateMachine.stateExited',
                   'State Exited',
                   [BreakpointParameter(
                       'targetElementType', objectType='stateMachine.state')],
                   description='Breaks when a specific state is about to be exited.'),

    BreakpointType('stateMachine.transitionFired',
                   'Transition Fired',
                   [BreakpointParameter(
                       'targetElementType', objectType='stateMachine.transition')],
                   'Breaks when a specific transition is about to be fired.')
]


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
            self.registry.loaded_sources[args.source_file], args.inputs)

        next_transition = self.runtimes[args.source_file].next_transition

        return InitResponse(next_transition is None)

    def get_breakpoint_types(self) -> GetBreakpointTypesResponse:
        return GetBreakpointTypesResponse(breakpoints)

    def next_step(self, source_file: str) -> StepResponse:
        """Performs a next step action in the runtime associated to a given source file.

        Args:
            source_file (str): source file for which to initialize the execution.

        Returns:
            StepResponse: response with the result of the performed step.
        """

        self._check_runtime_exists(source_file)
        next_transition = self.runtimes[source_file].next_step()

        return StepResponse(next_transition is None)

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

        runtime: Runtime = self.runtimes[source_file]
        if runtime.next_transition is None:
            raise ExecutionAlreadyDoneError()

        return GetRuntimeStateResponse(RuntimeState(self.runtimes[source_file]))

    def check_breakpoint(self, args: CheckBreakpointArgs) -> CheckBreakpointResponse:
        """Checks whether a breakpoint is activated.

        Args:
            args (CheckBreakpointArgs): arguments required to check a breakpoint.

        Returns:
            CheckBreakpointResponse: response with the result of the breakpoint checking.
        """
        self._check_runtime_exists(args.sourceFile)

        return self.runtimes[args.sourceFile].check_breakpoint(args.typeId, args.elementId)

    def _check_runtime_exists(self, source_file: str) -> None:
        """Checks that a runtime exists for a given source file.

        Args:
            source_file (str): source file for which to search for a runtime.

        Raises:
            ValueError: raised if no runtime is found.
        """

        if self.runtimes[source_file] is None:
            raise ValueError(f'No runtime for source file {source_file}.')
