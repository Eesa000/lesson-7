age = int(input("Enter your age: "))

# Using nested if-else statements to check the condition
if age >= 10:
    if age <= 20:
        print("Your age is between 10 and 20 years.")
    else:
        print("Your age is more than 20 years.")
else:
    print("Your age is less than 10 years.")