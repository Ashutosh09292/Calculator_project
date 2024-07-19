import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User input for password length
length = int(input("Enter the length of the password: "))

# Generate and display the random password
password = generate_password(length)
print("Generated Password:", password)