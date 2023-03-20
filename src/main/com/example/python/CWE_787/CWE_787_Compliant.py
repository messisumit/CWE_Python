my_list = [1, 2, 3, 4, 5]

# Try to write a value to an out of bounds index
try:
    my_list[5] = 6  # This will cause an out of bounds write error
except IndexError:
    print("Error: index out of range")