my_list = [1, 2, 3, 4, 5]

# Free the list object from memory
del my_list

# Access the list object using a try-except block
try:
    print(my_list)
except NameError:
    print("Error: variable not defined")