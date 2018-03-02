class Users:
    def __init__(self):
        self.users = {}
    def add_user(self,name,password,type):
        self.user[name] = password
        self.user[name].append(password)
        self.user[name].append(type)
        return {"Message":"User created successfully"}

