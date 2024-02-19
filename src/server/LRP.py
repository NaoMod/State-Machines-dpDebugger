from __future__ import annotations

from abc import abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import Any

from server.Utils import generate_uuid


@dataclass
class Arguments:
    sourceFile: str


class Response:
    @abstractmethod
    def to_dict(self) -> dict:
        pass


@dataclass
class ParseArguments(Arguments):
    pass


@dataclass
class ParseResponse(Response):
    astRoot: ModelElement

    def to_dict(self) -> dict:
        return {"astRoot": self.astRoot.to_dict()}


@dataclass
class InitializeExecutionArguments(Arguments):
    bindings: dict


class InitializeExecutionResponse(Response):
    def to_dict(self) -> dict:
        return {}


@dataclass
class GetBreakpointTypesResponse(Response):
    breakpointTypes: list[BreakpointType] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {"breakpointTypes": [bt.to_dict() for bt in self.breakpointTypes]}


@dataclass
class ExecuteAtomicStepArguments(Arguments):
    stepId: str


@dataclass
class ExecuteAtomicStepResponse(Response):
    completedSteps: list[str]

    def to_dict(self) -> dict:
        return self.__dict__


@dataclass
class GetRuntimeStateArguments(Arguments):
    pass


@dataclass
class GetRuntimeStateResponse(Response):
    runtimeStateRoot: ModelElement

    def to_dict(self) -> dict:
        return {"runtimeStateRoot": self.runtimeStateRoot.to_dict()}


@dataclass
class CheckBreakpointArguments(Arguments):
    typeId: str
    stepId: str
    bindings: dict


@dataclass
class CheckBreakpointResponse(Response):
    isActivated: bool
    message: str | None = None

    def to_dict(self) -> dict:
        res: dict[str, Any] = {"isActivated": self.isActivated}

        if self.isActivated and self.message is not None:
            res["message"] = self.message

        return res


@dataclass
class ModelElement:
    types: list[str]
    id: str = field(default_factory=generate_uuid)

    def construct_dict(self, attributes: dict, children: dict, refs: dict) -> dict:
        return {
            "id": self.id,
            "types": self.types,
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
class BreakpointType:
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
    PRIMITIVE = "primitive"
    OBJECT = "object"


class PrimitiveType(Enum):
    BOOLEAN = "boolean"
    STRING = "string"
    NUMBER = "number"


@dataclass
class GetAvailableStepsArguments(Arguments):
    pass


@dataclass
class GetAvailableStepsResponse(Response):
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
class EnterCompositeStepArguments(Arguments):
    stepId: str


class EnterCompositeStepResponse(Response):
    def to_dict(self) -> dict:
        return {}


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
class GetStepLocationResponse(Response):
    location: Location | None = None

    def to_dict(self) -> dict:
        res: dict[str, Any] = {}

        if self.location is not None:
            res["location"] = self.location.to_dict()

        return res
