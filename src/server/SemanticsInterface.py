from __future__ import annotations

import statemachine_ast.ASTRegistry as astRegistryModule

from server.LRP import (BreakpointParameter, BreakpointType,
                        CheckBreakpointArgs, CheckBreakpointResponse,
                        GetBreakpointTypesResponse, GetRuntimeStateResponse,
                        InitArguments, InitResponse, RuntimeState,
                        StepResponse)
from server.Runtime import Runtime

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
        runtimes (dict[str, Runtime]): Map of source files to their runtime
        registry (statemachine_ls.statemachine_ast.ASTRegistry.ASTRegistry): Registry of all already parsed ASTs.
    """

    def __init__(self, registry: astRegistryModule.ASTRegistry) -> None:
        self.runtimes: dict[str, Runtime] = {}
        self.registry: astRegistryModule.ASTRegistry = registry

    def initExecution(self, args: InitArguments) -> InitResponse:
        """Creates a new runtime for a given source file.
        The AST for the given source file must have been previously constructed.

        Args:
            args (InitArguments): Arguments required to start an execution.
        """

        self.runtimes[args.sourceFile] = Runtime(
            self.registry.loadedSources[args.sourceFile], args.inputs)

        nextTransition = self.runtimes[args.sourceFile].nextTransition

        return InitResponse(nextTransition is None)

    def getBreakpointTypes(self) -> GetBreakpointTypesResponse:
        return GetBreakpointTypesResponse(breakpoints)

    def nextStep(self, sourceFile: str) -> StepResponse:
        """Performs a next step action in the runtime associated to a given source file.

        Args:
            args (StepArguments): Arguments required to perform a step action.

        Returns:
            StepResponse: Response with the result of the performed step.
        """

        self._checkRuntimeExists(sourceFile)
        nextTransition = self.runtimes[sourceFile].nexStep()

        return StepResponse(nextTransition is None)

    def getRuntimeState(self, sourceFile: str) -> GetRuntimeStateResponse:
        """Returns the runtime state for a given source file.

        Args:
            sourceFile (str): Source file for which to return the runtime state

        Raises:
            Exception: Raised if the execution is done.

        Returns:
            RuntimeState: Runtime state for the source file.
        """

        self._checkRuntimeExists(sourceFile)

        runtime: Runtime = self.runtimes[sourceFile]
        if runtime.nextTransition is None:
            raise Exception('Execution done, no runtime state.')

        return GetRuntimeStateResponse(RuntimeState(self.runtimes[sourceFile]))

    def checkBreakpoint(self, args: CheckBreakpointArgs) -> CheckBreakpointResponse:
        self._checkRuntimeExists(args.sourceFile)

        return self.runtimes[args.sourceFile].checkBreakpoint(args.typeId, args.elementId)

    def _checkRuntimeExists(self, sourceFile: str) -> None:
        """Checks that a runtime exists for a given source file.

        Args:
            sourceFile (str): Source file for which to search for a runtime.

        Raises:
            Exception: Raised if no runtime is found.
        """

        if self.runtimes[sourceFile] is None:
            raise Exception('No runtime for source file \'' +
                            sourceFile + '\'.')
