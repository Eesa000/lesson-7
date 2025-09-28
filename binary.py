def decimal_to_binary(n):
    binary = ""

    while n > 0:

        remainder = n % 2 # get remainder

        binary = str(remainder) + binary # build the binary string

        n = n // 2 # reduce the number

    return binary if binary != "" else "0"

# Main Program
print("Decimal to Binary Conversion")
decimal_number = int(float(input("Enter a decimal number (whole numbers only): ")))
binary_number = decimal_to_binary(decimal_number)
print(f"Binary equivalent of {decimal_number} is: {binary_number}")
# Decimal to Binary Conversion using while loop 

            