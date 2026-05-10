for i in range(3):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == "admin" and password ==  "1234":
        print("Login Successfully")
        break
    else:
        print("Invalid Credentials")
else:
    print("Account Locked, Too many attempts")
