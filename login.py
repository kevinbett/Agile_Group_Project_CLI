from user_signup import Users

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    for user in Users:
        if user == username:
            return "Welcome, you are logged in"
        else:
            return "wrong password"

login()

                

