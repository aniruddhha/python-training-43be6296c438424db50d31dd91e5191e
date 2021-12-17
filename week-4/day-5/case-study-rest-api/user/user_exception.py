class InvalidUserNameException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(str)


class InvalidPasswordException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(str)


class InvalidRoleException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(str)


class InvalidUserException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(str)
