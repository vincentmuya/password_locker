#!/user/bin/env python3.6
from password_locker import Password

def create_password(aname,uname,email,password):
        new_password = Password(aname,uname,email,password)
        return new_password

def save_password(password):
        password.save_password()

def delete_password(password):
        password.delete_password()

def find_password(account_name):
    return Password.find_by_account_name(account_name)

def checking_existing_passwords(user_name):
    return Password.password_exist(user_name)

def display_passwords():
    return Password.display_passwords()

def main():
    print("Hello Welcome to password locker. Whats your name?")
    user_name = input()
    print("")

    print(f"Hi {user_name}! What would you like to do?")
    print("")


if __name__=='__main__':
    main()
