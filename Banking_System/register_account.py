# =======library imports==========#
import os
import json
# =======User inputs==============#
print('Project Banking System')
print('Register Account')

# Initialize variables
def credentials():
    client_name = input('Enter Your Full Name: ')
    age = input('Enter your age: ')
    # phone= input('Enter 10 Digit Number: ')
    # address = input('Enter your address: ')
    # email = input('Enter your email: ')

    # Security Client_Name Always have String Value
    if any(char.isdigit() for char in client_name):
       print('')
    
        
         
credentials()








# new_user = {
#     "name": client_name,
#     "lname": age,
#     'age': age,
#     'address': address,
#     'email': email
# }


# def options():
#     global client_name, age, address, email
#     client_name = input('Enter your name: ')
#     age = int(input('Enter your age: '))
#     address = input('Enter your address: ')
#     email = input('Enter your email: ')
    














