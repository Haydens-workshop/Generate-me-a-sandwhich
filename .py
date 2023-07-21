#==================================================================================
# Let's generate a password and a random username !
#==================================================================================

import random
import string
import os

def password_generator(length=32):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def random_username(length=12):
    characters = string.ascii_lowercase + string.digits
    username = ''.join(random.choice(characters) for _ in range(length))
    return f"{username}"

generated_username = random_username()
generated_password = password_generator()


file_content = f"Username: {generated_username}\nPassword: {generated_password}"

#==================================================================================
# Prepare the content for the file // 
# Check if the file already exists, and if it does, add a unique identifier

file_count = 0
file_name = f"{generated_username}.txt"
while os.path.exists(file_name):
    file_count += 1
    file_name = f"{generated_username}_{file_count}.txt"
#==================================================================================


# Exporting to the file with a unique name
with open(file_name, "w") as file:
    file.write(file_content)

# Let's share the exciting news!

#==================================================================================

print(f"Random username combo created and saved as '{file_name}'!")
