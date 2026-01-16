class UserAccount:
    def __init__(self, password):
        self._password = password

    def login(self, password):
        return password == self._password

    def change_password(self, old_password, new_password):
        if old_password == self._password:
            self._password = new_password


user = UserAccount("123")

print(user.login("123"))
print(user.login("000"))

user.change_password("123", "abc")
print(user.login("abc"))