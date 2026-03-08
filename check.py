# Test dictionary
test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}

# Print the dictionary
print("Test Dictionary:", test_dict)

# Ask the user for the value
value = int(input("Enter the value to check frequency: "))

# Count frequency
frequency = list(test_dict.values()).count(value)

# Print the result
print("Frequency of value", value, "is:", frequency)