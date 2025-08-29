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
    phone= input('Enter 10 Digit Number: ')
    address = input('Enter your address: ')
    email = input('Enter your email: ')
    

    # Security Client_Name Always have String Value
    if any(char.isdigit() for char in client_name):
      print('Not a Valid Client Name')
      credentials()
      if not age.isdigit():
       print('Not a Valid Age Input')
       credentials()   
      if not phone.isdigit() and len(phone) != 10:
        print('Not a Valid Input or Digits are less')
        credentials()
      if not (email.endswith('@gmail.com') or email.endswith('@yahoo.com')):
        print('Not a Valid Email Id')
        credentials() 

    else:
        print(f'Name: {client_name}')  
        print(f'Age: {age}')  
        print(f'Phone: {phone}')  
        print(f'Address: {address}')
        print(f'Email: {email}')
          

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
    














