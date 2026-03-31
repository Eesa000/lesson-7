# Task 1: Odd numbers below a user-input value

# take a number from the user
n = int(input("Enter a positive integer: "))

# list of all odd numbers under n using list comprehension
odd_numbers = [i for i in range(1, n) if i % 2 != 0]

print("Odd numbers below", n, "are:", odd_numbers)


# Task 2: Capitalize first letter of each fruit

# original list of fruits (you can change these)
fruits = ["apple", "banana", "mango", "orange", "grape"]

# new list with first letter capitalized using list comprehension
capitalized_fruits = [fruit.capitalize() for fruit in fruits]

print("Original fruits:", fruits)
print("Capitalized fruits:", capitalized_fruits)