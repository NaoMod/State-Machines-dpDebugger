from __future__ import annotations

import uuid
from abc import abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import Any

from server.Runtime import Runtime

"""---------------- Base protocol ----------------"""


@dataclass
class Arguments:
    sourceFile: str


@dataclass
class ModelElement:
    type: str
    id: str = str(uuid.uuid4())

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
        return {
            "breakpointTypes": list(
                map(lambda breakpoint: breakpoint.to_dict(), self.breakpointTypes)
            )
        }


@dataclass
class StepArguments(Arguments):
    threadId: int | None = None
    stepId: str | None = None


@dataclass
class StepResponse:
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
            "parameters": list(map(lambda param: param.to_dict(), self.parameters)),
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
        return {
            "steppingModes": list(map(lambda mode: mode.to_dict(), self.steppingModes))
        }


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

    def to_dict(self) -> dict:
        return {
            "availableSteps": list(
                map(lambda step: step.to_dict(), self.availableSteps)
            )
        }


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
            res["location"] = self.location

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


class RuntimeState(ModelElement):
    """Represents the current state of a runtime.
    Contains the information passed to the debugger.

    Attributes:
        inputs (list[str]): ordered symbols given as inputs for the execution.
        next_consumed_input_index (int | None): index of the next input to consume. None if there is no input left.
        current_state (State): current state in the state machine.
        outputs (list[str]): outputs created so far during the execution.
    """

    def __init__(self, runtime: Runtime) -> None:
        super().__init__("stateMachine.runtimeState")
        self.inputs = runtime.inputs
        self.next_consumed_input_index = (
            None
            if runtime.available_transitions is None
            else runtime.next_consumed_input_index
        )
        self.current_state = runtime.current_state
        self.outputs = runtime.outputs
        self.variables = runtime.variables

    def to_dict(self) -> dict:
        if self.current_state.is_final:
            return super().construct_dict(
                {
                    "inputs": self.inputs,
                    "nextConsumedInputIndex": self.next_consumed_input_index,
                    "outputs": self.outputs,
                    "currentState": "FINAL"
                },
                {"variables": VariablesRegistry(self.variables).to_dict()},
                {},
            )

        return super().construct_dict(
            {
                "inputs": self.inputs,
                "nextConsumedInputIndex": self.next_consumed_input_index,
                "outputs": self.outputs
            },
            {"variables": VariablesRegistry(self.variables).to_dict()},
            {"currentState": self.current_state.id},
        )

class VariablesRegistry(ModelElement):
    variables: dict[str, float]

    def __init__(self, variables: dict[str, float]) -> None:
        super().__init__("stateMachine.variablesRegistry")
        self.variables = variables

    def to_dict(self) -> dict:
        return super().construct_dict(self.variables, {}, {})