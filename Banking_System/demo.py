import json
import os

# Take user input
name = input("Enter your first name: ")
lname = input("Enter your last name: ")

# New user entry
new_user = {
    "name": name,
    "lname": lname
}

# JSON file path
file_path = "client_data.json"

# Load existing data if the file exists, otherwise start with an empty list
if os.path.exists(file_path):
    with open(file_path, "r") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            data = []
else:
    data = []

# Append the new user
data.append(new_user)

# Save the updated data back to the file
with open(file_path, "w") as file:
    json.dump(data, file, indent=4)

print("User data added successfully.")

