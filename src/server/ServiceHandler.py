from __future__ import annotations

from parser.StateMachineLexer import StateMachineLexer
from parser.StateMachineParser import StateMachineParser

import statemachine_ast.ASTRegistry as astRegistryModule
from antlr4 import CommonTokenStream, FileStream
from server.ExposedTypes import breakpoints
from server.LRP import (
    CheckBreakpointArguments,
    CheckBreakpointResponse,
    EnterCompositeStepArguments,
    EnterCompositeStepResponse,
    ExecuteAtomicStepArguments,
    ExecuteAtomicStepResponse,
    GetAvailableStepsArguments,
    GetAvailableStepsResponse,
    GetBreakpointTypesResponse,
    GetRuntimeStateArguments,
    GetRuntimeStateResponse,
    GetStepLocationArguments,
    GetStepLocationResponse,
    InitializeExecutionArguments,
    InitializeExecutionResponse,
    ParseArguments,
    ParseResponse,
)
from server.Runtime import Runtime, RuntimeState
from statemachine_ast.BuildASTVisitor import BuildASTVisitor
from statemachine_ast.StateMachine import StateMachine


class ServiceHandler:
    """Implements LRP services.

    Attributes:
        runtimes (dict[str, Runtime]): map of source files to their runtime.
        registry (ASTRegistry): registry of all already parsed ASTs.
    """

    def __init__(self) -> None:
        self.runtimes: dict[str, Runtime] = {}
        self.registry: astRegistryModule.ASTRegistry = astRegistryModule.ASTRegistry()

    def parse(self, args: ParseArguments) -> ParseResponse:
        """Parses a file and stores the generated StateMachine in self.registry.

        Args:
            args (ParseArguments): arguments of the request.

        Returns:
            ParseResponse: response to the request.
        """

        text_input = FileStream(args.sourceFile)
        lexer = StateMachineLexer(text_input)
        stream = CommonTokenStream(lexer)
        parser = StateMachineParser(stream)
        tree = parser.statemachine()

        visitor = BuildASTVisitor()
        state_machine: StateMachine = visitor.visitStatemachine(tree)
        self.registry.set_ast(args.sourceFile, state_machine)
        if args.sourceFile in self.runtimes:
            del self.runtimes[args.sourceFile]

        return ParseResponse(state_machine)

    def initialize_execution(
        self, args: InitializeExecutionArguments
    ) -> InitializeExecutionResponse:
        """Creates a new runtime for a given source file.
        The AST for the given source file must have been previously constructed.

        Args:
            args (InitializeExecutionArguments): arguments of the request.

        Returns:
            InitializeExecutionResponse: response to the request.
        """

        self.runtimes[args.sourceFile] = Runtime(
            self.registry.loaded_sources[args.sourceFile]
        )

        return InitializeExecutionResponse()

    def get_runtime_state(
        self, args: GetRuntimeStateArguments
    ) -> GetRuntimeStateResponse:
        """Returns the current runtime state for a given source file.

        Args:
            args (GetRuntimeStateArguments): arguments of the request.

        Raises:
            ValueError: raised if no runtime exists for the given source file.

        Returns:
            GetRuntimeStateResponse: response to the request.
        """

        self._check_runtime_exists(args.sourceFile)

        return GetRuntimeStateResponse(RuntimeState(self.runtimes[args.sourceFile]))

    def get_breakpoint_types(self) -> GetBreakpointTypesResponse:
        """Returns the breakpoint types exposed by the language runtime.

        Returns:
            GetBreakpointTypesResponse: response to the request.
        """

        return GetBreakpointTypesResponse(breakpoints)

    def check_breakpoint(
        self, args: CheckBreakpointArguments
    ) -> CheckBreakpointResponse:
        """Checks whether a breakpoint is activated.

        Args:
            args (CheckBreakpointArgs): arguments of the request.

        Raises:
            ValueError: raised if no runtime exists for the given source file.

        Returns:
            CheckBreakpointResponse: response to the request.
        """

        self._check_runtime_exists(args.sourceFile)

        return self.runtimes[args.sourceFile].check_breakpoint(
            args.typeId, args.stepId, args.bindings
        )

    def get_available_steps(
        self, args: GetAvailableStepsArguments
    ) -> GetAvailableStepsResponse:
        """Returns the available steps from the current runtime state.
        Influenced by calls to enterCompositeStep and executeAtomicStep.

        Args:
            args (GetAvailableStepsArguments): arguments of the request.

        Raises:
            ValueError: raised if no runtime exists for the given source file.

        Returns:
            GetAvailableStepsResponse: response to the request.
        """

        self._check_runtime_exists(args.sourceFile)

        runtime = self.runtimes[args.sourceFile]
        available_steps = list(runtime.compute_available_steps().values())
        parent_step = (
            available_steps[0].parent_step if len(available_steps) > 0 else None
        )

        return GetAvailableStepsResponse(
            [step.to_LRP_step() for step in available_steps],
            parent_step.id if parent_step is not None else None,
        )

    def enter_composite_step(
        self, args: EnterCompositeStepArguments
    ) -> EnterCompositeStepResponse:
        """Enters a composite step and render available the steps it contains.
        Steps are listed through getAvailableSteps.

        Args:
            args (EnterCompositeStepArguments): arguments of the request.

        Raises:
            ValueError: raised if no runtime exists for the given source file.

        Returns:
            EnterCompositeStepResponse: response to the request.
        """

        self._check_runtime_exists(args.sourceFile)
        self.runtimes[args.sourceFile].enter_composite_step(args.stepId)

        return EnterCompositeStepResponse()

    def execute_atomic_step(
        self, args: ExecuteAtomicStepArguments
    ) -> ExecuteAtomicStepResponse:
        """Performs a single atomic step in the runtime associated to a given source file.
        Steps are listed through getAvailableSteps.

        Args:
            args (ExecuteAtomicStepArguments): arguments of the request.

        Raises:
            ValueError: raised if no runtime exists for the given source file.

        Returns:
            ExecuteAtomicStepResponse: response to the request.
        """

        self._check_runtime_exists(args.sourceFile)
        executed_step = self.runtimes[args.sourceFile].execute_atomic_step(args.stepId)

        return ExecuteAtomicStepResponse(
            [x.id for x in executed_step.get_completed_steps()]
        )

    def get_step_location(
        self, args: GetStepLocationArguments
    ) -> GetStepLocationResponse:
        """Returns the location of a step.
        Steps are listed through getAvailableSteps.

        Args:
            args (GetStepLocationArguments): arguments of the request.

        Raises:
            ValueError: raised if no runtime exists for the given source file.

        Returns:
            GetStepLocationResponse: response to the request.
        """

        self._check_runtime_exists(args.sourceFile)
        step = self.runtimes[args.sourceFile].available_steps.get(args.stepId)
        assert step is not None, f"No step with id {args.stepId}."

        return GetStepLocationResponse(step.location)

    def _check_runtime_exists(self, source_file: str) -> None:
        """Checks that a runtime exists for a given source file.

        Args:
            source_file (str): source file for which to search for a runtime.

        Raises:
            ValueError: raised if no runtime exists for the given source file.
        """

        if self.runtimes[source_file] is None:
            raise ValueError(f"No runtime for source file {source_file}.")
