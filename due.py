# Read input values
X, Y, C = map(int, input("Enter X Y C separated by space: ").split())

# Calculate the maximum number of apples Walter can buy with his money
max_by_money = Y // X

# The answer is the minimum of what he can buy and the safe limit
max_apples = min(max_by_money, C)

print(max_apples)
