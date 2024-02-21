from server.LRP import BreakpointParameter, BreakpointParameterType, BreakpointType

breakpoints: list[BreakpointType] = [
    BreakpointType(
        "stateReached",
        "State Reached",
        "Breaks when a specific state is about to be reached.",
        [BreakpointParameter("s", BreakpointParameterType.OBJECT, objectType="State")],
    ),
    BreakpointType(
        "stateExited",
        "State Exited",
        "Breaks when a specific state is about to be exited.",
        [BreakpointParameter("s", BreakpointParameterType.OBJECT, objectType="State")],
    ),
    BreakpointType(
        "transitionFired",
        "Transition Fired",
        "Breaks when a specific transition is about to be fired.",
        [BreakpointParameter("t", BreakpointParameterType.OBJECT, objectType="Transition")],
    ),
    BreakpointType(
        "assignmentEvaluated",
        "Assignment Evaluated",
        "Breaks when a specific assignment is about to be evaluated.",
        [BreakpointParameter("a", BreakpointParameterType.OBJECT, objectType="Assignment")],
    ),
]
