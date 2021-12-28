class InvalidCustomerMobileException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)


class InvalidCustomerNameException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
