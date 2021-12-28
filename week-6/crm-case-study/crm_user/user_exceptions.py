class UserNotFoundException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
        self.msg = msg


class InActiveUserException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
        self.msg = msg
