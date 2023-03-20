import os

def delete_file(file_path):

    os.remove(file_path)
    print("File deleted successfully.")

# Call the delete_file function without authenticating the user
delete_file("/path/to/file.txt")