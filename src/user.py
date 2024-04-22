class User:
    def __init__(self, username:str, password:str):
        self.username = username
        self.password = password

    def edit_password(self, new_password):
        self.password = new_password