def get_sensitive_data():
    username = "my_username"
    password = "my_password"
    return username, password

# Call the get_sensitive_data function
username, password = get_sensitive_data()

# Print the sensitive data to the console (exposing it to unauthorized users/actors)
print("Username: ", username)
print("Password: ", password)