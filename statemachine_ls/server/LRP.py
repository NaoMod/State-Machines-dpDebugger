from __future__ import annotations

import uuid
from abc import abstractmethod
from typing import Any
from enum import Enum

import statemachine_ast.StateMachine as stateMachineModule

from server.Runtime import Runtime

"""---------------- Base protocol ----------------"""


class ModelElement:

    def __init__(self, type: str) -> None:
        self.id = str(uuid.uuid4())
        self.type = type

    def constructDict(self, attributes: dict, children: dict, refs: dict) -> dict:
        return {
            'id': self.id,
            'type': self.type,
            'attributes': attributes,
            'children': children,
            'refs': refs
        }

    @abstractmethod
    def toDict(self) -> dict:
        pass


class ASTElement(ModelElement):

    def __init__(self, type: str, location: Location | None = None) -> None:
        super().__init__(type)
        self.location = location

    def constructDict(self, attributes: dict, children: dict, refs: dict) -> dict:
        return super().constructDict(attributes, children, refs) if self.location is None else {
            **super().constructDict(attributes, children, refs),
            'location': self.location.toDict()
        }

    @abstractmethod
    def toDict(self) -> dict:
        pass


class Location:

    def __init__(self, line: int, endLine: int, column: int, endColumn: int) -> None:
        self.line = line
        self.column = column
        self.endLine = endLine
        self.endColumn = endColumn

    def toDict(self) -> dict:
        return self.__dict__


class ParseResponse:

    def __init__(self, astRoot: ModelElement) -> None:
        self.astRoot = astRoot

    def toDict(self) -> dict:
        return {
            'astRoot': self.astRoot.toDict()
        }


class InitResponse:

    def __init__(self, isExecutionDone: bool = False) -> None:
        self.isExecutionDone = isExecutionDone

    def toDict(self) -> dict:
        return self.__dict__

class GetBreakpointTypesResponse:

    def __init__(self, breakpointTypes: list[BreakpointType] | None = None) -> None:
        self.breakpointTypes = [] if breakpointTypes is None else breakpointTypes

    def toDict(self) -> dict:
        return {
            'breakpointTypes': list(map(lambda breakpoint: breakpoint.toDict(), self.breakpointTypes))
        }

class StepResponse:
    """Represents the response to the execution of a step action.
    A step is defined as the transition between two coherent runtime states.

    Attributes:
        nextCompletedStep (Step): Next atomic step to be completed.
    """

    def __init__(self, isExecutionDone: bool = False) -> None:
        self.isExecutionDone = isExecutionDone

    def toDict(self) -> dict:
        return self.__dict__


class Step:

    def __init__(self, type: str, info: dict) -> None:
        self.type = type
        self.info = info

    def toDict(self) -> dict:
        return self.__dict__


class BreakpointType:

    def __init__(self, id: str, name: str, parameters: list[BreakpointParameter], description: str = '') -> None:
        self.id = id
        self.parameters = parameters
        self.name = name
        self.description = description

    def toDict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'parameters': list(map(lambda param: param.toDict(), self.parameters))
        }


class BreakpointParameter:

    def __init__(self, name: str, primitiveType: PrimitiveType | None = None, objectType: str | None = None,  isMultivalued: bool = False) -> None:
        self.name = name
        self.primitiveType = primitiveType
        self.objectType = objectType
        self.isMultivalued = isMultivalued

    def toDict(self) -> dict:
        res = {
            'name': self.name,
            'isMultivalued': self.isMultivalued
        }

        if not self.primitiveType is None:
            res = {
                **res,
                'primitiveType': self.primitiveType.value
            }
        
        if not self.objectType is None:
            res = {
                **res,
                'objectType': self.objectType
            }

        return res

class PrimitiveType(Enum):
    BOOLEAN = 'boolean'
    STRING = 'string'
    NUMBER = 'number'


class GetRuntimeStateResponse:

    def __init__(self, runtimeStateRoot: ModelElement) -> None:
        self.runtimeStateRoot = runtimeStateRoot

    def toDict(self) -> dict:
        return {
            'runtimeStateRoot': self.runtimeStateRoot.toDict()
        }


class CheckBreakpointArgs:

    def __init__(self, sourceFile: str, typeId: str, elementId: str) -> None:
        self.sourceFile = sourceFile
        self.typeId = typeId
        self.elementId = elementId


class CheckBreakpointResponse:

    def __init__(self, isActivated: bool, message: str | None = None) -> None:
        self.isActivated = isActivated
        self.message = message

    def toDict(self) -> dict:
        res: dict[str, Any] = {
            'isActivated': self.isActivated
        }

        if not self.message is None:
            res['message'] = self.message

        return res


"""---------------- Domain-specific ----------------"""


class InitArguments:
    """Arguments required to start an execution.

    Attributes:
        sourceFile (str): Source file for which to initialize the execution.
        inputs (list[str]): Ordered symbols given as inputs for the execution.
    """

    def __init__(self, sourceFile: str, inputs: list[str]) -> None:
        self.sourceFile: str = sourceFile
        self.inputs: list[str] = inputs


class TransitionStep(Step):

    def __init__(self, nextTransition: stateMachineModule.Transition) -> None:
        super().__init__('stateMachine.transition',
                         {'transition': nextTransition.id})


class RuntimeState(ModelElement):
    """Represents the current state of a runtime.
    Contains the information passed to the debugger.

    Attributes:
        variables (list[Variable]): Variables of the runtime.
        possibleSteps (list[PossibleStep]): Possible next steps.
    """

    def __init__(self, runtime: Runtime) -> None:
        super().__init__('stateMachine.runtimeState')
        self.inputs = runtime.inputs
        self.nextConsumedInputIndex = runtime.nextConsumedInputIndex
        self.currentState = runtime.currentState
        self.outputs = runtime.outputs

    def toDict(self) -> dict:
        return super().constructDict(
            {
                'inputs': self.inputs,
                'nextConsumedInputIndex': self.nextConsumedInputIndex,
                'outputs': self.outputs
            },
            {},
            {
                'currentState': self.currentState.id
            }
        )
