from user import User

class UserService:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def list_users(self):
        list = []
        for user in self.users:
            list.append(user.username)
        return list
    
    def check_login(self, username:str, password:str):
        for user in self.users:
            if user.username == username and user.password == password:
                return True
            else:
                return False