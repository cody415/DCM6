# Recursive function to calculate length of a list
def array_length_recursive(arr):
    # Base case: empty list has length 0
    if arr == []:
        return 0
    else:
        # Recursive case: 1 + length of the rest of the list
        return 1 + array_length_recursive(arr[1:])

# Example usage
my_list = [10, 20, 30, 40, 50]
print("Length of the list is:", array_length_recursive(my_list))
