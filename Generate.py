import secrets
import string
import os
from datetime import datetime

def password_generator(length=40, min_digits=6, min_special=4):
    # Ensuring the password meets complexity requirements
    if min_digits + min_special > length:
        raise ValueError("Length must be greater than the sum of minimum digits and special characters required")
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = []
    
    #==================================================================================
    # Adding required digits and special characters first
    password.extend(secrets.choice(string.digits) for _ in range(min_digits))
    password.extend(secrets.choice(string.punctuation) for _ in range(min_special))

    #==================================================================================
    # Filling the rest of the password length with random characters
    password.extend(secrets.choice(characters) for _ in range(length - min_digits - min_special))

    
    #==================================================================================
    # Shuffling to avoid predictable patterns
    secrets.SystemRandom().shuffle(password)
    
    return ''.join(password)

def random_username(length=12):
    characters = string.ascii_lowercase + string.digits
    username = ''.join(secrets.choice(characters) for _ in range(length))
    return username

generated_username = random_username()
generated_password = password_generator()

file_content = f"Username: {generated_username}\nPassword: {generated_password}"

#==================================================================================
# Prepare the content for the file // 
# Check if the file already exists, and if it does, add a unique identifier

file_count = 0
file_name = f"{generated_username}.txt"
unique_suffix = secrets.token_hex(4)
while os.path.exists(f"{file_name}_{unique_suffix}"):
    unique_suffix = secrets.token_hex(4)
file_name = f"{file_name}_{unique_suffix}.txt"
 # Regenerate if collision occurs , doubtful -- but it can happen

#==================================================================================


with open(file_name, "w") as file:
    file.write(file_content)
    
# Exporting to the file with a unique name and secure random suffix
#==================================================================================

print(f"Random combo created and saved as '{file_name}'!")
