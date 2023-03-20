def credentials(username, password):
    if username == "default" and password == "password":
        print("Login successful")
    else:
        print("Invalid username or password")


username = input("Enter your username: ")
password = input("Enter your password: ")      # There is no check for the strength of the password or any other security measure
credentials(username, password)