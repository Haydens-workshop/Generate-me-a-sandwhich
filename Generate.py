import secrets
import string
import os
from datetime import datetime

def password_generator(length=40, min_digits=6, min_special=4):
#=====================================================================================================================================
    #Generate a password of specified length with at least a certain number of digits and special characters.
#=====================================================================================================================================
    Args:
    length (int): Total length of the password.
    min_digits (int): Minimum required digits in the password.
    min_special (int): Minimum required special characters in the password.

    Returns:
    str: The generated password.
    """
    if min_digits + min_special > length:
        raise ValueError("Length must be greater than the sum of minimum digits and special characters required")
    
    characters = string.ascii_letters + string.digits + string.punctuation
    random = secrets.SystemRandom()  
#=====================================================================================================================================
    # Using a single instance for random operations
#=====================================================================================================================================
    

    password = [
        *random.choices(string.digits, k=min_digits),
        *random.choices(string.punctuation, k=min_special),
        *random.choices(characters, k=length - min_digits - min_special)
    ]
    
    random.shuffle(password)
    return ''.join(password)

def random_username(length=12):
#=====================================================================================================================================
  #  Generates a random username.
   # Args:
    #length (int): Length of the username.

    #Returns:
    #str: The generated username.
#=====================================================================================================================================
    characters = string.ascii_lowercase + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))

generated_username = random_username()
generated_password = password_generator()

file_content = f"Username: {generated_username}\nPassword: {generated_password}"

# Ensure the file name is unique
file_count = 0
file_name = f"{generated_username}.txt"
unique_suffix = secrets.token_hex(4)
while os.path.exists(f"{file_name}_{unique_suffix}"):
    unique_suffix = secrets.token_hex(4)
file_name = f"{file_name}_{unique_suffix}.txt"

try:
    with open(file_name, "w") as file:
        file.write(file_content)
    print(f"Random combo created and saved as '{file_name}'!")
except IOError as e:
    print(f"Failed to write to file: {e}")
