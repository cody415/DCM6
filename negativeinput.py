def take_input():
    num = int(input("Enter a number: "))
    
    # Base case: stop when a negative number is entered
    if num < 0:
        print("Negative number entered. Stopping recursion.")
        return
    else:
        print("You entered:", num)
        # Recursive call
        take_input()

# Start the recursion
take_input()
