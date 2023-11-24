from server.LRP import BreakpointParameter, BreakpointType, SteppingMode

breakpoints: list[BreakpointType] = [
    BreakpointType(
        "stateMachine.stateReached",
        "State Reached",
        [BreakpointParameter("targetElementType", objectType="stateMachine.state")],
        "Breaks when a specific state is about to be reached.",
    ),
    BreakpointType(
        "stateMachine.stateExited",
        "State Exited",
        [BreakpointParameter("targetElementType", objectType="stateMachine.state")],
        description="Breaks when a specific state is about to be exited.",
    ),
    BreakpointType(
        "stateMachine.transitionFired",
        "Transition Fired",
        [
            BreakpointParameter(
                "targetElementType", objectType="stateMachine.transition"
            )
        ],
        "Breaks when a specific transition is about to be fired.",
    ),
    BreakpointType(
        "stateMachine.assignmentEvaluated",
        "Assignment Evaluated",
        [
            BreakpointParameter(
                "targetElementType", objectType="stateMachine.assignment"
            )
        ],
        description="Breaks when a specific assignment is about to be evaluated.",
    ),
]

steppingModes: list[SteppingMode] = [
    SteppingMode("stateMachine.atomicStep", "Atomic Step", ""),
    SteppingMode(
        "stateMachine.scopedTransition",
        "Scoped Transition Step",
        "Fires the next transition at a given depth.",
    ),
]
