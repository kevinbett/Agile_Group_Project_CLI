class Users:
    def __init__(self):
        self.users = {}
        self.password = password
        self.userType = utype
    def add_user(self,name,password,userType):
        self.user[name] = password
        self.user[name].append(password)
        self.user[name].append(userType)
        return {"Message":"User created successfully"}


class Admin(Users):
	def __init__(self):
		self.admin = {}

	def add_comment(self,commet):
		self.admim[name] = commet
		return {"message": "Comment added sucesfully"}

	def delete_comment(self,name):
		del self.admin[name]
		return {"message": "comment deleted sucesfully"}


	def edit_comment(self,name):
		del self.admin[name]
		return {"message": "comment editted sucesfully"}

	def view_comment(self):
		return self.admin
