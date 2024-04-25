from .LRP import (
    BreakpointParameter,
    BreakpointType,
    CheckBreakpointResponse,
    EnterCompositeStepResponse,
    ExecuteAtomicStepResponse,
    GetAvailableStepsResponse,
    GetBreakpointTypesResponse,
    GetRuntimeStateResponse,
    GetStepLocationResponse,
    InitializeExecutionResponse,
    Location,
    ModelElement,
    ParseResponse,
    Step,
)


def from_model_element(model_element: ModelElement) -> dict:
    res: dict = {
        "id": model_element.id,
        "types": model_element.types,
        "attributes": model_element.attributes,
        "children": {
            key: (
                [from_model_element(subvalue) for subvalue in value]
                if isinstance(value, list)
                else from_model_element(value)
            )
            for (key, value) in zip(
                model_element.children.keys(), model_element.children.values()
            )
        },
        "refs": model_element.refs,
    }

    if model_element.location is not None:
        res["location"] = from_location(model_element.location)

    return res


def from_breakpoint_type(breakpoint_type: BreakpointType) -> dict:
    return {
        "id": breakpoint_type.id,
        "name": breakpoint_type.name,
        "description": breakpoint_type.description,
        "parameters": [
            from_breakpoint_parameter(param) for param in breakpoint_type.parameters
        ],
    }


def from_breakpoint_parameter(parameter: BreakpointParameter) -> dict:
    res: dict = {
        "name": parameter.name,
        "isMultivalued": parameter.isMultivalued,
        "type": parameter.type.value,
    }

    if parameter.primitiveType is not None:
        res = {**res, "primitiveType": parameter.primitiveType.value}

    if parameter.objectType is not None:
        res = {**res, "objectType": parameter.objectType}

    return res


def from_step(step: Step) -> dict:
    res: dict = {
        "id": step.id,
        "name": step.name,
        "isComposite": step.isComposite,
    }

    if step.description is not None:
        res["description"] = step.description

    return res


def from_location(location: Location) -> dict:
    return location.__dict__


def from_parse_response(response: ParseResponse) -> dict:
    return {"astRoot": from_model_element(response.astRoot)}


def from_initialize_execution_response(response: InitializeExecutionResponse) -> dict:
    return {}


def from_get_breakpoint_types_response(response: GetBreakpointTypesResponse) -> dict:
    return {
        "breakpointTypes": [from_breakpoint_type(bt) for bt in response.breakpointTypes]
    }


def from_execute_atomic_step_response(response: ExecuteAtomicStepResponse) -> dict:
    return response.__dict__


def from_get_runtime_state_response(response: GetRuntimeStateResponse) -> dict:
    return {"runtimeStateRoot": from_model_element(response.runtimeStateRoot)}


def from_check_breakpoint_response(response: CheckBreakpointResponse) -> dict:
    res: dict = {"isActivated": response.isActivated}

    if response.isActivated and response.message is not None:
        res["message"] = response.message

    return res


def from_get_available_steps_response(response: GetAvailableStepsResponse) -> dict:
    return {"availableSteps": [from_step(step) for step in response.availableSteps]}


def from_enter_composite_step_response(response: EnterCompositeStepResponse) -> dict:
    return {}


def from_get_step_location_response(response: GetStepLocationResponse) -> dict:
    res: dict = {}

    if response.location is not None:
        res["location"] = from_location(response.location)

    return res
