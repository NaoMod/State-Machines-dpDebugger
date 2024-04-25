from __future__ import annotations

from abc import abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import Any

from server.Utils import generate_uuid


@dataclass
class Arguments:
    """Arguments to a LRP request.

    Attributes:
        sourceFile (str): Source file targeted by the request.
    """

    sourceFile: str


class Response:
    """Response to an LRP request."""

    @abstractmethod
    def to_dict(self) -> dict:
        pass


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

    def to_dict(self) -> dict:
        return {"astRoot": self.astRoot.to_dict()}


@dataclass
class InitializeExecutionArguments(Arguments):
    """Arguments for the 'initializeExecution' LRP request.

    Attributes:
        sourceFile (str): source file targeted by the request.
        bindings: (dict): arbitrary arguments necessary for the initialization of a runtime state.
    """

    bindings: dict


class InitializeExecutionResponse(Response):
    """Response to the 'initializeExecution' LRP request."""

    def to_dict(self) -> dict:
        return {}


@dataclass
class GetBreakpointTypesResponse(Response):
    """Response to the 'getBreakpointTypes' LRP request.

    Attributes:
        breakpointTypes (list[BreakpointType]): breakpoint types defined by the language runtime.
    """

    breakpointTypes: list[BreakpointType] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {"breakpointTypes": [bt.to_dict() for bt in self.breakpointTypes]}


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

    def to_dict(self) -> dict:
        return self.__dict__


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

    def to_dict(self) -> dict:
        return {"runtimeStateRoot": self.runtimeStateRoot.to_dict()}


@dataclass
class CheckBreakpointArguments(Arguments):
    """Arguments for the 'checkBreakpoint' LRP request.

    Attributes:
        sourceFile (str): source file targeted by the request.
        typeId (str): identifier of the breakpoint type.
        stepId (str): identifier of the step on which to check the breakpoint.
        bindings (dict): arbitrary arguments required to check the breakpoint.
    """

    typeId: str
    stepId: str
    bindings: dict


@dataclass
class CheckBreakpointResponse(Response):
    """Response to the 'checkBreakpoint' LRP request.

    Attributes:
        isActivated (bool): true if the breakpoint is activated, false otherwise.
        message (str | None): human-readable message to describe the cause of activation. Should only be set if `isActivated` is true.
    """

    isActivated: bool
    message: str | None = None

    def to_dict(self) -> dict:
        res: dict[str, Any] = {"isActivated": self.isActivated}

        if self.isActivated and self.message is not None:
            res["message"] = self.message

        return res


@dataclass
class ModelElement:
    """Element of the AST or runtime state.

    Attributes:
        id (str): unique identifier of the element.
        types (list[str]): types of the element.
        location (Location | None): location of the element in its original source file.
    """

    types: list[str]
    id: str = field(default_factory=generate_uuid)
    location: Location | None = None

    def construct_dict(self, attributes: dict, children: dict, refs: dict) -> dict:
        res: dict = {
            "id": self.id,
            "types": self.types,
            "attributes": attributes,
            "children": children,
            "refs": refs,
        }

        if self.location is not None:
            res["location"] = self.location.to_dict()

        return res

    @abstractmethod
    def to_dict(self) -> dict:
        pass


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

    def to_dict(self) -> dict:
        return self.__dict__


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

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "parameters": [param.to_dict() for param in self.parameters],
        }


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

    def to_dict(self) -> dict:
        res = {
            "name": self.name,
            "isMultivalued": self.isMultivalued,
            "type": self.type.value,
        }

        if self.primitiveType is not None:
            res = {**res, "primitiveType": self.primitiveType.value}

        if self.objectType is not None:
            res = {**res, "objectType": self.objectType}

        return res


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

    def to_dict(self) -> dict:
        return {"availableSteps": [step.to_dict() for step in self.availableSteps]}


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

    def to_dict(self) -> dict:
        return {}


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

    def to_dict(self) -> dict:
        res: dict[str, Any] = {
            "id": self.id,
            "name": self.name,
            "isComposite": self.isComposite,
        }

        if self.description is not None:
            res["description"] = self.description

        return res


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

    def to_dict(self) -> dict:
        res: dict[str, Any] = {}

        if self.location is not None:
            res["location"] = self.location.to_dict()

        return res
