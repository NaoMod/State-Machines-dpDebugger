from server.LRP import BreakpointParameter, BreakpointParameterType, BreakpointType

breakpoints: list[BreakpointType] = [
    BreakpointType(
        "stateReached",
        "State Reached",
        [BreakpointParameter("s", BreakpointParameterType.ELEMENT, elementType="State")],
        "Breaks when a specific state is about to be reached.",
    ),
    BreakpointType(
        "stateExited",
        "State Exited",
        [BreakpointParameter("s", BreakpointParameterType.ELEMENT, elementType="State")],
        "Breaks when a specific state is about to be exited.",
    ),
    BreakpointType(
        "transitionFired",
        "Transition Fired",
        [BreakpointParameter("t", BreakpointParameterType.ELEMENT, elementType="Transition")],
        "Breaks when a specific transition is about to be fired.",
    ),
    BreakpointType(
        "assignmentExecuted",
        "Assignment Executed",
        [BreakpointParameter("a", BreakpointParameterType.ELEMENT, elementType="Assignment")],
        "Breaks when a specific assignment is about to be executed.",
    ),
]
