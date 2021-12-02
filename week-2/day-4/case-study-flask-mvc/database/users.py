
class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role


class UserDatabase:

    def __init__(self):
        self.users = [
            User('abc', 'abc', 'admin'),
            User('pqr', 'pqr', 'user')
        ]

    def user_by_creds(self, username, password) -> User:
        for user in self.users:
            if(user.username == username and user.password == password):
                return user

        return None
