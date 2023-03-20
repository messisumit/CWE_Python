# Define a function that retrieves sensitive data


def get_sensitive_data():
    username = "my_username"
    password = "my_password"
    return username, password

# Call the get_sensitive_data function
username, password = get_sensitive_data()

# Use the sensitive data in a secure way (e.g. authenticate the user)
def authenticate_user(username, password):
    return True


if authenticate_user(username, password):
    print("User authenticated successfully.")
else:
    print("Error: authentication failed.")
