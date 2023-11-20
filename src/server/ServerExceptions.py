class UnknownBreakpointTypeError(ValueError):
    """Error raised when an unknown breakpoint type id is given
    as an argument of an LRP request.

    Attributes:
        breakpoint_type_id (str): the unknown breakpoint type id.
    """

    def __init__(self, breakpoint_type_id: str, *args: object) -> None:
        super().__init__(*args)
        self.breakpoint_type_id = breakpoint_type_id

    def __str__(self) -> str:
        return f"Unknown breakpoint type {self.breakpoint_type_id}."


class ExecutionAlreadyDoneError(Exception):
    """Error raised when an LRP request is called on a source file
    whose execution is already done.
    """

    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self) -> str:
        return "Execution already done."
