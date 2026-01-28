# Recursive function to calculate power of 2
def power_of_two(n):
    # Base case
    if n == 0:
        return 1
    else:
        # Recursive case
        return 2 * power_of_two(n - 1)

# Example usage
num = int(input("Enter the exponent: "))
print(f"2^{num} = {power_of_two(num)}")
