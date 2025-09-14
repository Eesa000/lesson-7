# Program to print a mirrored right-angled triangle

def mirrored_triangle(n):
    for i in range(1, n + 1):
        # Print spaces first
        print(" " * (n - i) + "*" * i)

# Example usage:
rows = int(input("Enter the number of rows: "))
mirrored_triangle(rows)
