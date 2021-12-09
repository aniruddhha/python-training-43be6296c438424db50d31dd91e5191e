
class InvalidDateException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
