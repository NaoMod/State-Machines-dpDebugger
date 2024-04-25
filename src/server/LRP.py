from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


@dataclass
class Arguments:
    """Arguments to a LRP request.

    Attributes:
        sourceFile (str): Source file targeted by the request.
    """

    sourceFile: str


class Response:
    """Response to an LRP request."""


@dataclass
class ParseArguments(Arguments):
    """Arguments for the 'parse' LRP request.

    Attributes:
        sourceFile (str): source file targeted by the request.
    """

    pass


@dataclass
class ParseResponse(Response):
    """Response to the 'parse' LRP request.

    Attributes:
        astRoot (ModelElement): root of the AST.
    """

    astRoot: ModelElement


@dataclass
class InitializeExecutionArguments(Arguments):
    """Arguments for the 'initializeExecution' LRP request.

    Attributes:
        sourceFile (str): source file targeted by the request.
        bindings: (dict[str, Any]): arbitrary arguments necessary for the initialization of a runtime state.
    """

    bindings: dict[str, Any]


class InitializeExecutionResponse(Response):
    """Response to the 'initializeExecution' LRP request."""

    pass


@dataclass
class GetBreakpointTypesResponse(Response):
    """Response to the 'getBreakpointTypes' LRP request.

    Attributes:
        breakpointTypes (list[BreakpointType]): breakpoint types defined by the language runtime.
    """

    breakpointTypes: list[BreakpointType] = field(default_factory=list)


@dataclass
class ExecuteAtomicStepArguments(Arguments):
    """Arguments for the 'executeAtomicStep' LRP request.

    Attributes:
        sourceFile (str): source file targeted by the request.
        stepId (str): identifier of the atomic step to execute.
    """

    stepId: str


@dataclass
class ExecuteAtomicStepResponse(Response):
    """Response to the 'executeAtomicStep' LRP request.

    Attributes:
        completedSteps (list[str]): identifiers of the steps completed after the execution of the atomic step.
    """

    completedSteps: list[str]


@dataclass
class GetRuntimeStateArguments(Arguments):
    """Arguments for the 'getRuntimeState' LRP request.

    Attributes:
        sourceFile (str): source file targeted by the request.
    """

    pass


@dataclass
class GetRuntimeStateResponse(Response):
    """Response to the 'getRuntimeState' LRP request.

    Attributes:
        runtimeStateRoot (ModelElement): root of the runtime state.
    """

    runtimeStateRoot: ModelElement


@dataclass
class CheckBreakpointArguments(Arguments):
    """Arguments for the 'checkBreakpoint' LRP request.

    Attributes:
        sourceFile (str): source file targeted by the request.
        typeId (str): identifier of the breakpoint type.
        stepId (str): identifier of the step on which to check the breakpoint.
        bindings ([str, Any]): arbitrary arguments required to check the breakpoint.
    """

    typeId: str
    stepId: str
    bindings: dict[str, Any]


@dataclass
class CheckBreakpointResponse(Response):
    """Response to the 'checkBreakpoint' LRP request.

    Attributes:
        isActivated (bool): true if the breakpoint is activated, false otherwise.
        message (str | None): human-readable message to describe the cause of activation. Should only be set if `isActivated` is true.
    """

    isActivated: bool
    message: str | None = None


@dataclass
class ModelElement:
    """Element of the AST or runtime state.

    Attributes:
        id (str): unique identifier of the element.
        types (list[str]): types of the element.
        attributes (dict[str, Any]): attributes with primitive values.
        children (dict[str, ModelElement] | list[ModelElement]): containment relations with other elements.
        refs (dict[str, str | list[str]]): references to other elements.
        location (Location | None): location of the element in its original source file.
    """

    id: str
    types: list[str]
    attributes: dict[str, Any]
    children: dict[str, ModelElement | list[ModelElement]]
    refs: dict[str, str | list[str]]
    location: Location | None = None


@dataclass
class Location:
    """Location in a textual source file.

    Attributes:
        line (int): starting line.
        endLine (int): starting column.
        column (int): end line.
        endColumn (int): end column.
    """

    line: int
    endLine: int
    column: int
    endColumn: int


@dataclass
class BreakpointType:
    """Breakpoint type defined by the language runtime.

    Attributes:
        id (str): unique identifier of the breakpoint type.
        name (str): human-readable name of the breakpoint type.
        description (str): human-readable description of the breakpoint type.
        parameters (list[BreakpointParameter]): parameters needed to evaluate a breakpoint of this type.
    """

    id: str
    name: str
    description: str
    parameters: list[BreakpointParameter]


@dataclass
class BreakpointParameter:
    """Parameter required by a breakpoint type.

    Attributes:
        name (str): name of the parameter.
        type (BreakpointParameterType): type of the parameter.
        isMultivalued (bool): true is the parameter is a collection, false otherwise.
        primitiveType (PrimitiveType | None): primitive type of the parameter. Exactly one of `primitiveType` and `objectType` must be set.
        objectType (str | None): object type of the object parameter. If the object is a model element, the type is the same as defined in `ModelElement.types`. Exactly one of `primitiveType` and `objectType` must be set.
    """

    name: str
    type: BreakpointParameterType
    isMultivalued: bool = False
    primitiveType: PrimitiveType | None = None
    objectType: str | None = None


class BreakpointParameterType(Enum):
    """Type of a breakpoint parameter."""

    PRIMITIVE = "primitive"
    OBJECT = "object"


class PrimitiveType(Enum):
    """Primitive type of a value."""

    BOOLEAN = "boolean"
    STRING = "string"
    NUMBER = "number"


@dataclass
class GetAvailableStepsArguments(Arguments):
    """Arguments for the 'getAvailableSteps' LRP request.

    Attributes:
        sourceFile (str): source file targeted by the request.
    """

    pass


@dataclass
class GetAvailableStepsResponse(Response):
    """Response to the 'getAvailableSteps' LRP request.

    Attributes:
        availableSteps (list[Step]): currently available steps.
    """

    availableSteps: list[Step]


@dataclass
class EnterCompositeStepArguments(Arguments):
    """Arguments for the 'enterCompositeStep' LRP request.

    Attributes:
        sourceFile (str): source file targeted by the request.
        stepId (str): identifier of the composite step to enter.
    """

    stepId: str


class EnterCompositeStepResponse(Response):
    """Response to the 'enterCompositeStep' LRP request."""

    pass


@dataclass
class Step:
    """Execution step.

    Attributes:
        id (str): unique identifier of the step.
        name (str): human-readable name of the step.
        isComposite (bool): true if the step is composite, false otherwise.
        description (str | None): human-readable description of the step.
    """

    id: str
    name: str
    isComposite: bool
    description: str | None = None


@dataclass
class GetStepLocationArguments(Arguments):
    """Arguments for the 'getStepLocation' LRP request.

    Attributes:
        sourceFile (str): source file targeted by the request.
        stepId (str): identifier of the step for which to retrieve the location.
    """

    stepId: str


@dataclass
class GetStepLocationResponse(Response):
    """Response to the 'getStepLocation' LRP request.

    Attributes:
        location (Location | None): location of the step.
    """

    location: Location | None = None
