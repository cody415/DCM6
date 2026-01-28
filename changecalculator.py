# Recursive function to count ways to make change
def countWays(coins, n, total):
    # Base cases
    if total == 0:
        return 1   # Found a valid way
    if total < 0:
        return 0   # Invalid way
    if n <= 0 and total >= 1:
        return 0   # No coins left but total still > 0

    # Two choices:
    # 1. Include the coin (reduce total by coin value, keep n same)
    # 2. Exclude the coin (reduce n by 1)
    return countWays(coins, n, total - coins[n-1]) + countWays(coins, n-1, total)


# Example usage
coins = [1, 2, 5]   # denominations
amount = int(input("Enter the amount
