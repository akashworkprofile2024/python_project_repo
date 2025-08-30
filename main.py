import subprocess  # run Another script in one go means python file run in another python file

def main():
    print('Choose an action:')
    print('1. Register Account')
    print('2. Login Account')
    
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        subprocess.run(['python3', 'register_account.py'])    
    elif choice == '2':
        subprocess.run(['python3', 'Client_login.py'])
    else:
        print('Invalid choice')       
main()
