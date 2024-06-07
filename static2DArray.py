# Static 2D Array
static_array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Function to print the 2D array
def print_array(array):
    for row in array:
        for elem in row:
            print(elem, end=' ')
        print()

print("Static 2D Array:")
print_array(static_array)
