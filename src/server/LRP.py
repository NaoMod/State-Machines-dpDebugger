from __future__ import annotations

from abc import abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import Any

from server.Utils import generate_uuid

"""---------------- Base protocol ----------------"""


@dataclass
class Arguments:
    sourceFile: str


@dataclass
class ModelElement:
    type: str
    id: str = field(default_factory=generate_uuid)

    def construct_dict(self, attributes: dict, children: dict, refs: dict) -> dict:
        return {
            "id": self.id,
            "type": self.type,
            "attributes": attributes,
            "children": children,
            "refs": refs,
        }

    @abstractmethod
    def to_dict(self) -> dict:
        pass


@dataclass
class ASTElement(ModelElement):
    location: Location | None = None
    step_location: Location | None = None

    def construct_dict(self, attributes: dict, children: dict, refs: dict) -> dict:
        return (
            super().construct_dict(attributes, children, refs)
            if self.location is None
            else {
                **super().construct_dict(attributes, children, refs),
                "location": self.location.to_dict(),
            }
        )

    @abstractmethod
    def to_dict(self) -> dict:
        pass


@dataclass
class Location:
    line: int
    endLine: int
    column: int
    endColumn: int

    def to_dict(self) -> dict:
        return self.__dict__


@dataclass
class ParseResponse:
    astRoot: ModelElement

    def to_dict(self) -> dict:
        return {"astRoot": self.astRoot.to_dict()}


@dataclass
class InitResponse:
    isExecutionDone: bool = False

    def to_dict(self) -> dict:
        return self.__dict__


@dataclass
class GetBreakpointTypesResponse:
    breakpointTypes: list[BreakpointType] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {"breakpointTypes": [bt.to_dict() for bt in self.breakpointTypes]}


@dataclass
class StepArguments(Arguments):
    threadId: int | None = None
    stepId: str | None = None


@dataclass
class StepResponse:
    completedSteps: list[str]
    isExecutionDone: bool = False

    def to_dict(self) -> dict:
        return self.__dict__


@dataclass
class BreakpointType:
    id: str
    name: str
    parameters: list[BreakpointParameter]
    description: str = ""

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "parameters": [param.to_dict() for param in self.parameters],
        }


@dataclass
class BreakpointParameter:
    name: str
    primitiveType: PrimitiveType | None = None
    objectType: str | None = None
    isMultivalued: bool = False

    def to_dict(self) -> dict:
        res = {"name": self.name, "isMultivalued": self.isMultivalued}

        if self.primitiveType is not None:
            res = {**res, "primitiveType": self.primitiveType.value}

        if self.objectType is not None:
            res = {**res, "objectType": self.objectType}

        return res


class PrimitiveType(Enum):
    BOOLEAN = "boolean"
    STRING = "string"
    NUMBER = "number"


@dataclass
class GetRuntimeStateResponse:
    runtimeStateRoot: ModelElement

    def to_dict(self) -> dict:
        return {"runtimeStateRoot": self.runtimeStateRoot.to_dict()}


@dataclass
class CheckBreakpointArguments(Arguments):
    typeId: str
    elementId: str
    stepId: str | None = None


@dataclass
class CheckBreakpointResponse:
    isActivated: bool
    message: str | None = None

    def to_dict(self) -> dict:
        res: dict[str, Any] = {"isActivated": self.isActivated}

        if self.message is not None:
            res["message"] = self.message

        return res


@dataclass
class InitializeResponse:
    capabilities: LanguageRuntimeCapabilities

    def to_dict(self) -> dict:
        return {"capabilities": self.capabilities.to_dict()}


@dataclass
class LanguageRuntimeCapabilities:
    supportsThreads: bool
    supportsStackTrace: bool
    supportsScopes: bool

    def to_dict(self) -> dict:
        return self.__dict__


@dataclass
class GetSteppingModesResponse:
    steppingModes: list[SteppingMode]

    def to_dict(self) -> dict:
        return {"steppingModes": [mode.to_dict() for mode in self.steppingModes]}


@dataclass
class SteppingMode:
    id: str
    name: str
    description: str

    def to_dict(self) -> dict:
        return self.__dict__


@dataclass
class GetAvailableStepsArguments(Arguments):
    steppingModeId: str
    compositeStepId: str | None = None


@dataclass
class GetAvailableStepsResponse:
    availableSteps: list[Step]
    parentStepId: str | None = None

    def to_dict(self) -> dict:
        result: dict = {
            "availableSteps": [step.to_dict() for step in self.availableSteps]
        }

        if self.parentStepId is not None:
            result["parentStepId"] = self.parentStepId

        return result


@dataclass
class Step:
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
    stepId: str


@dataclass
class GetStepLocationResponse:
    location: Location | None = None

    def to_dict(self) -> dict:
        res: dict[str, Any] = {}

        if self.location is not None:
            res["location"] = self.location.to_dict()

        return res


"""---------------- Domain-specific ----------------"""


@dataclass
class InitArguments:
    """Arguments required to start an execution.

    Attributes:
        source_file (str): source file for which to initialize the execution.
        inputs (list[str]): ordered symbols given as inputs for the execution.
    """

    source_file: str
    inputs: list[str]
