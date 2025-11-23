def check_age():
    age_input = input("Please enter your age: ")

    try:
        age = int(age_input)
        if age < 0:
            print("Error: Age cannot be negative.")
        elif age % 2 == 0:
            print(f"The age {age} is even.")
        else:
            print(f"The age {age} is odd.")
    except ValueError:
        print("Value Error: Please enter a valid integer age (no decimals, letters, or special characters).")

if __name__ == "__main__":
    check_age()
