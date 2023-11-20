from __future__ import annotations

import uuid
from abc import abstractmethod
from enum import Enum
from typing import Any

from server.Runtime import Runtime

"""---------------- Base protocol ----------------"""

class Arguments:
    def __init__(self, sourceFile: str) -> None:
        self.sourceFile = sourceFile


class ModelElement:
    def __init__(self, type: str) -> None:
        self.id = str(uuid.uuid4())
        self.type = type

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


class ASTElement(ModelElement):
    def __init__(self, type: str, location: Location | None = None) -> None:
        super().__init__(type)
        self.location = location

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


class Location:
    def __init__(self, line: int, endLine: int, column: int, endColumn: int) -> None:
        self.line = line
        self.column = column
        self.endLine = endLine
        self.endColumn = endColumn

    def to_dict(self) -> dict:
        return self.__dict__


class ParseResponse:
    def __init__(self, astRoot: ModelElement) -> None:
        self.astRoot = astRoot

    def to_dict(self) -> dict:
        return {"astRoot": self.astRoot.to_dict()}


class InitResponse:
    def __init__(self, isExecutionDone: bool = False) -> None:
        self.isExecutionDone = isExecutionDone

    def to_dict(self) -> dict:
        return self.__dict__


class GetBreakpointTypesResponse:
    def __init__(self, breakpointTypes: list[BreakpointType] | None = None) -> None:
        self.breakpointTypes = [] if breakpointTypes is None else breakpointTypes

    def to_dict(self) -> dict:
        return {
            "breakpointTypes": list(
                map(lambda breakpoint: breakpoint.to_dict(), self.breakpointTypes)
            )
        }


class StepArguments(Arguments):
    def __init__(
        self, sourceFile: str, threadId: int | None = None, stepId: str | None = None
    ) -> None:
        super().__init__(sourceFile)
        self.threadId = threadId
        self.stepId = stepId


class StepResponse:
    def __init__(self, isExecutionDone: bool = False) -> None:
        self.isExecutionDone = isExecutionDone

    def to_dict(self) -> dict:
        return self.__dict__


class BreakpointType:
    def __init__(
        self,
        id: str,
        name: str,
        parameters: list[BreakpointParameter],
        description: str = "",
    ) -> None:
        self.id = id
        self.parameters = parameters
        self.name = name
        self.description = description

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "parameters": list(map(lambda param: param.to_dict(), self.parameters)),
        }


class BreakpointParameter:
    def __init__(
        self,
        name: str,
        primitiveType: PrimitiveType | None = None,
        objectType: str | None = None,
        isMultivalued: bool = False,
    ) -> None:
        self.name = name
        self.primitiveType = primitiveType
        self.objectType = objectType
        self.isMultivalued = isMultivalued

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


class GetRuntimeStateResponse:
    def __init__(self, runtimeStateRoot: ModelElement) -> None:
        self.runtimeStateRoot = runtimeStateRoot

    def to_dict(self) -> dict:
        return {"runtimeStateRoot": self.runtimeStateRoot.to_dict()}


class CheckBreakpointArguments(Arguments):
    def __init__(
        self, sourceFile: str, typeId: str, elementId: str, stepId: str | None = None
    ) -> None:
        super().__init__(sourceFile)
        self.typeId = typeId
        self.elementId = elementId
        self.stepId = stepId


class CheckBreakpointResponse:
    def __init__(self, isActivated: bool, message: str | None = None) -> None:
        self.isActivated = isActivated
        self.message = message

    def to_dict(self) -> dict:
        res: dict[str, Any] = {"isActivated": self.isActivated}

        if self.message is not None:
            res["message"] = self.message

        return res


class InitializeResponse:
    def __init__(self, capabilities: LanguageRuntimeCapabilities) -> None:
        self.capabilities = capabilities

    def to_dict(self) -> dict:
        return {"capabilities": self.capabilities.to_dict()}


class LanguageRuntimeCapabilities:
    def __init__(
        self, supportsThreads: bool, supportsStackTrace: bool, supportsScopes: bool
    ) -> None:
        self.supportsThreads = supportsThreads
        self.supportsStackTrace = supportsStackTrace
        self.supportsScopes = supportsScopes

    def to_dict(self) -> dict:
        return self.__dict__


class GetSteppingModesResponse:
    def __init__(self, steppingModes: list[SteppingMode]) -> None:
        self.steppingModes = steppingModes

    def to_dict(self) -> dict:
        return {
            "steppingModes": list(map(lambda mode: mode.to_dict(), self.steppingModes))
        }


class SteppingMode:
    def __init__(self, id: str, name: str, description: str) -> None:
        self.id = id
        self.name = name
        self.description = description

    def to_dict(self) -> dict:
        return self.__dict__


class GetAvailableStepsArguments(Arguments):
    def __init__(
        self, sourceFile: str, steppingModeId: str, compositeStepId: str | None = None
    ) -> None:
        super().__init__(sourceFile)
        self.steppingModeId = steppingModeId
        self.compositeStepId = compositeStepId


class GetAvailableStepsResponse:
    def __init__(self, availableSteps: list[Step]) -> None:
        self.availableSteps = availableSteps

    def to_dict(self) -> dict:
        return {
            "availableSteps": list(
                map(lambda step: step.to_dict(), self.availableSteps)
            )
        }


class Step:
    def __init__(
        self, id: str, name: str, isComposite: bool, description: str | None = None
    ) -> None:
        self.id = id
        self.name = name
        self.isComposite = isComposite
        self.description = description

    def to_dict(self) -> dict:
        res: dict[str, Any] = {
            "id": self.id,
            "name": self.name,
            "isComposite": self.isComposite,
        }

        if self.description is not None:
            res["description"] = self.description

        return res


class GetStepLocationArguments(Arguments):
    def __init__(self, sourceFile: str, stepId: str) -> None:
        super().__init__(sourceFile)
        self.stepId = stepId


class GetStepLocationResponse:
    def __init__(self, location: Location | None = None) -> None:
        self.location = location

    def to_dict(self) -> dict:
        res: dict[str, Any] = {}

        if self.location is not None:
            res["location"] = self.location

        return res


"""---------------- Domain-specific ----------------"""


class InitArguments:
    """Arguments required to start an execution.

    Attributes:
        source_file (str): source file for which to initialize the execution.
        inputs (list[str]): ordered symbols given as inputs for the execution.
    """

    def __init__(self, source_file: str, inputs: list[str]) -> None:
        self.source_file: str = source_file
        self.inputs: list[str] = inputs


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

    def to_dict(self) -> dict:
        if self.current_state.is_final:
            return super().construct_dict(
                {
                    "inputs": self.inputs,
                    "nextConsumedInputIndex": self.next_consumed_input_index,
                    "outputs": self.outputs,
                    "currentState": "FINAL",
                },
                {},
                {},
            )

        return super().construct_dict(
            {
                "inputs": self.inputs,
                "nextConsumedInputIndex": self.next_consumed_input_index,
                "outputs": self.outputs,
            },
            {},
            {"currentState": self.current_state.id},
        )
