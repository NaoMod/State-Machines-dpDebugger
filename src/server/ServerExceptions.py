class UnknownBreakpointTypeError(ValueError):

    def __init__(self, breakpointTypeId: str, *args: object) -> None:
        super().__init__(*args)
        self.breakpointTypeId = breakpointTypeId

    def __str__(self) -> str:
        return f'Unknown breakpoint type {self.breakpointTypeId}.'


class ExecutionAlreadyDoneError(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self) -> str:
        return f'Execution already done.'
