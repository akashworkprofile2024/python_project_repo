import os
import json
import random
print('Project Banking System')
print('Register Account')

def generate_acc_number(acctype):
    if acctype.upper()=='S':
     fixed_prefix = "278755"   # first 6 fixed digits
     suffix = '01'
    else:
     fixed_prefix = '235428'
     suffix = '02'    
    random_digits = str(random.randint(1000, 9999))  # 4 random digits
    return fixed_prefix + random_digits + suffix  # total 12 digits

def generate_acc_pin():
    return str(random.randint(1000, 9999))  # 4-digit PIN
    
def credentials():
    while True:
        client_name = input('Enter Your Full Name: ')
        age = input('Enter your age: ')
        phone = input('Enter 10 Digit Number: ')
        address = input('Enter your address: ')
        email = input('Enter your email: ')
        acctype = input('Enter account type (S for Savings / C for Current): ')

        # === Validations ===
        if any(char.isdigit() for char in client_name):
            print('❌ Not a Valid Client Name')
            continue
        if not age.isdigit():
            print('❌ Not a Valid Age Input')
            continue
        if not phone.isdigit() or len(phone) != 10:
            print('❌ Phone must be 10 digits')
            continue
        if not (email.endswith('@gmail.com') or email.endswith('@yahoo.com')):
            print('❌ Not a Valid Email Id')
            continue

        # === Account type ===
        if acctype.upper() not in ['S', 'C']:
            print("❌ Invalid Account Type. Choose 'S' or 'C'.")
            continue  

        account_number = generate_acc_number(acctype)
        pin = generate_acc_pin()
        account_type = 'Savings Account' if acctype.upper() == 'S' else 'Current Account'          
        # If everything is valid → print details
        print("\n--- Account Created Successfully ---")
        print(f'Name: {client_name}')  
        print(f'Age: {age}')  
        print(f'Phone: {phone}')  
        print(f'Address: {address}')
        print(f'Email: {email}')
        print(f'Account-Type: {account_type}')
        print(f'Account-Type: {account_number}') 
        print(f'Account-PIN: {pin}') 
        print("✅ Registered Successfully ✅")
        break
     
credentials()
