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

def display_password():
    return Password.display_passwords()

def main():
    print("Hello Welcome to password locker. Whats your name?")
    user_name = input()
    print("")

    print(f"Hi {user_name}! What would you like to do?")
    print("")

    while True:
        print("""Use these short codes:
                ca - create new account,
                da - display account,
                fa - find account,
                ex - exit password locker.""")
        short_code = input().lower()
        print("_" * 20)
        if short_code == "ca":
            print("New Account")
            print("_" * 20)

            print("Enter Account Name -")
            a_name = input()

            print("Enter User Name -")
            u_name = input()

            print("Enter Email -")
            e_address = input()

            print("Enter Password -")
            a_password = input()

            save_password(create_password(a_name, u_name, e_address, a_password))

            print("")
            print(f"""New account - {a_name} {u_name} """)
            print("")

        elif short_code == "da":
            if display_password():
                print("Here is a list of all your accounts")
                print("")
                for password in display_passwords():
                    print(f"{password.account_name} {password.user_name} {password.email} {password.account_password}")
                    print("")
            else:
                print("")
                print("You dont seem to have any accounts saved yet")
                print("")



if __name__=='__main__':
    main()
