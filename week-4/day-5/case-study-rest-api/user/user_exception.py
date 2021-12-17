class InvalidUserNameException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(str)
        self.msg = msg


class InvalidPasswordException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(str)
        self.msg = msg


class InvalidRoleException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(str)
        self.msg = msg


class InvalidUserException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(str)
        self.msg = msg
