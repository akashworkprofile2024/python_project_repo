import os
import json
import random
def cls():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Mac/Linux
    else:
        os.system('clear')

#==============================  DATA CENTER SCHEMA ====================
# DATA_FILE = "C:\\Users\\Private\\Desktop\\Workspace_Folder\\Python_Project_Repo\\Banking_System\\datacenter\\client_accounts.json" # For Windows
DATA_FILE = '/opt/lampp/htdocs/gitfetch/Python_Project_Repo/Banking_System/datacenter/client_accounts.json' 

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

#==============================  DATA CENTER SCHEMA END ====================

# ====================   GENERATE PIN AND ACCOUNT NUMBER SCHEMA ===================
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

#=========================== GENERATE PIN AND ACCOUNT NUMBER SCHEMA =============== 
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
        # === VALIDATIONS END ===


        if acctype.upper() not in ['S', 'C']:
            print("❌ Invalid Account Type. Choose 'S' or 'C'.")
            continue  

        account_number = generate_acc_number(acctype)
        pin = generate_acc_pin()
        account_type = 'Savings Account' if acctype.upper() == 'S' else 'Current Account'          

#======================== PUSH INTO DATABASE ==========================
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

        # Append to list and save back to file
        accounts.append(new_user)
        save_data(accounts)
#======================== PUSH INTO DATABASE ========================== 

#======================== CILENT DETAILS ============================= 
        cls()
        print('\t\t\t\t\t\t\t\t NEO BANK')
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
#======================== CILENT DETAILS END ============================= 
credentials()
