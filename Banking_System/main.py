import subprocess  # run Another script in one go means python file run in another python file
import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    attempts = 0  # count wrong attempts

    while attempts < 3:
        cls()
        print('Welcome To Neo Bank')
        print('1. Register Account')
        print('2. Login Account')
        print('3. Admin Account')

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            subprocess.run(['python3', 'register_account.py'])
            break
        elif choice == '2':
            subprocess.run(['python3', 'Client_login.py'])
            break
        elif choice == '3':
            subprocess.run(['python3', 'Admin.py'])
            break
        else:
            print('Invalid choice. Please try again.')
            attempts += 1
            
    if attempts == 3:
        cls()
        print('⚠️  Too many invalid attempts. Please restart the program later.')

# Start the program
if __name__ == "__main__":
    main()
