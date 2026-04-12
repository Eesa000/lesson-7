import random
import string

def generate_password(length=12):
    # চরacters to use
    characters = string.ascii_letters + string.digits
    
    # generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Example usage
password_length = int(input("Enter password length: "))
print("Generated Password:", generate_password(password_length))