import os
import json
import random
# from twilio.rest import Client

#========== PASTE TWILIO CONFIGURATION FROM README.md ================


#========== PASTE TWILIO CONFIGURATION FROM README.md ================


DATA_FILE = '/opt/lampp/htdocs/gitfetch/Python_Project_Repo/Banking_System/datacenter/client_accounts.json'

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def generate_acc_number(acctype):
    fixed_prefix = "278755" if acctype.upper() == 'S' else '235428'
    suffix = '01' if acctype.upper() == 'S' else '02'
    random_digits = str(random.randint(1000, 9999))
    return fixed_prefix + random_digits + suffix

def generate_acc_pin():
    return str(random.randint(1000, 9999))

# ======================= OTP SCHEMA ==================

# ======================= OTP SCHEMA END ==================

def credentials():
    accounts = load_data()
    while True:
        cls()
        print('\t\t\t\t\t\t\t\t NEO BANK')
        print('Register Account')
        client_name = input('Enter Your Full Name: ')
        age = input('Enter your age: ')
        phone = input('Enter 10 Digit Number: ')
        address = input('Enter your address: ')
        email = input('Enter your email: ')
        acctype = input('Enter account type (S for Savings / C for Current): ')

        # === VALIDATIONS ===
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
        if acctype.upper() not in ['S', 'C']:
            print("❌ Invalid Account Type. Choose 'S' or 'C'.")
            continue

        # === SEND OTP ===
        
        #===  SENT OTP END ========

        # === Registration continues ===
        account_number = generate_acc_number(acctype)
        pin = generate_acc_pin()
        account_type = 'Savings Account' if acctype.upper() == 'S' else 'Current Account'

        new_user = {
            "account_number": account_number,
            "pin": pin,
            "name": client_name,
            "age": age,
            "phone": phone,
            "address": address,
            "email": email,
            "account_type": account_type
        }

        accounts.append(new_user)
        save_data(accounts)

        cls()
        print('\t\t\t\t\t\t\t\t NEO BANK')
        print("\n--- Account Created Successfully ---")
        print(f'Name: {client_name}')
        print(f'Age: {age}')
        print(f'Phone: {phone}')
        print(f'Address: {address}')
        print(f'Email: {email}')
        print(f'Account-Type: {account_type}')
        print(f'Account-Number: {account_number}')
        print(f'Account-PIN: {pin}')
        print("✅ Registered Successfully ✅")
        break

credentials()
