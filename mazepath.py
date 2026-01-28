# Recursive function to count maze paths
def maze_paths(m, n):
    # Base case: if rat is at the boundary (first row or first column)
    if m == 1 or n == 1:
        return 1
    
    # Recursive case:
    # Rat can move either down (m-1) or right (n-1)
    return maze_paths(m-1, n) + maze_paths(m, n-1)


# Example usage
rows = int(input("Enter number of rows in maze: "))
cols = int(input("Enter number of columns in maze: "))

ways = maze
