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
    """Exposes the services related to execution semantics.

    Attributes:
        runtimes (dict[str, Runtime]): map of source files to their runtime
        registry (ASTRegistry): registry of all already parsed ASTs.
    """

    def __init__(self, registry: astRegistryModule.ASTRegistry) -> None:
        self.runtimes: dict[str, Runtime] = {}
        self.registry: astRegistryModule.ASTRegistry = registry

    def parse(self, args: ParseArguments) -> ParseResponse:
        """Parses a file and stores the generated StateMachine in self.registry.

        Args:
            file (str): URI of the file to parse.
        """

        text_input = FileStream(args.sourceFile)
        lexer = StateMachineLexer(text_input)
        stream = CommonTokenStream(lexer)
        parser = StateMachineParser(stream)
        tree = parser.statemachine()

        visitor = BuildASTVisitor()
        state_machine: StateMachine = visitor.visitStatemachine(tree)
        self.registry.set_ast(args.sourceFile, state_machine)

        return ParseResponse(state_machine)

    def initialize_execution(
        self, args: InitializeExecutionArguments
    ) -> InitializeExecutionResponse:
        """Creates a new runtime for a given source file.
        The AST for the given source file must have been previously constructed.

        Args:
            args (InitArguments): arguments required to start an execution.

        Returns:
            InitResponse: response with the result of the initialization.
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
            source_file (str): source file for which to return the runtime state

        Raises:
            ExecutionAlreadyDoneError: raised if the execution is done.

        Returns:
            RuntimeState: current runtime state for the source file.
        """

        self._check_runtime_exists(args.sourceFile)

        return GetRuntimeStateResponse(RuntimeState(self.runtimes[args.sourceFile]))

    def get_breakpoint_types(self) -> GetBreakpointTypesResponse:
        return GetBreakpointTypesResponse(breakpoints)

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
            args.typeId, args.stepId, args.bindings
        )

    def get_available_steps(
        self, args: GetAvailableStepsArguments
    ) -> GetAvailableStepsResponse:
        self._check_runtime_exists(args.sourceFile)

        runtime = self.runtimes[args.sourceFile]
        available_steps = list(
            runtime.compute_available_steps(args.sourceFile).values()
        )
        parent_step = (
            available_steps[0].parent_step if len(available_steps) > 0 else None
        )

        return GetAvailableStepsResponse(
            [step.to_LRP_step() for step in available_steps],
            parent_step.id if parent_step is not None else None,
        )

    # TODO: implement enter composite step
    def enter_composite_step(
        self, args: EnterCompositeStepArguments
    ) -> EnterCompositeStepResponse:
        pass

    def execute_atomic_step(
        self, args: ExecuteAtomicStepArguments
    ) -> ExecuteAtomicStepResponse:
        """Performs a next step action in the runtime associated to a given source file.

        Args:
            source_file (str): source file for which to initialize the execution.

        Returns:
            StepResponse: response with the result of the performed step.
        """

        self._check_runtime_exists(args.sourceFile)
        executed_step = self.runtimes[args.sourceFile].execute_step(args.stepId)

        return ExecuteAtomicStepResponse(
            [x.id for x in executed_step.get_completed_steps()]
        )

    def get_step_location(
        self, args: GetStepLocationArguments
    ) -> GetStepLocationResponse:
        self._check_runtime_exists(args.sourceFile)
        step = self.runtimes[args.sourceFile].available_steps.get(args.stepId)
        assert step is not None, f"No step with id {args.stepId}."

        return GetStepLocationResponse(step.location)

    def _check_runtime_exists(self, source_file: str) -> None:
        """Checks that a runtime exists for a given source file.

        Args:
            source_file (str): source file for which to search for a runtime.

        Raises:
            ValueError: raised if no runtime is found.
        """

        if self.runtimes[source_file] is None:
            raise ValueError(f"No runtime for source file {source_file}.")
