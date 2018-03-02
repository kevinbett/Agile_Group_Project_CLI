from user_signup import Users

username = input("Enter your username: ")
password = input("Enter your password: ")

def login(username,password):
    for user in Users:
        if user == username:
            return "Welcome, you are logged in"
        else:
            return "wrong password"


                

