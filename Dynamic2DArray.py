# Dynamic 2D Array
dynamic_array = []

# Adding rows dynamically
dynamic_array.append([1, 2, 3])
dynamic_array.append([4, 5])
dynamic_array.append([6, 7, 8, 9])

# Function to print the 2D array
def print_array(array):
    for row in array:
        for elem in row:
            print(elem, end=' ')
        print()

print("Dynamic 2D Array:")
print_array(dynamic_array)

# Modifying the dynamic 2D array
dynamic_array[1].append(6)
dynamic_array.append([10, 11, 12])

print("Modified Dynamic 2D Array:")
print_array(dynamic_array)
