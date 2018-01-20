#!/user/bin/env python3.6
import getpass
from password_locker import User, Password

def create_user(locker_userName, locker_password):
        new_user = User(locker_userName, locker_password)
        return new_user

def save_user(user):
        user.save_user()

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
    print("Hello welcome to password locker")
    while True:
        print(
            """Use these shortcode:
                si - sign in
                lg - log in""")
        short_code = input().lower()
        print("_" * 20)
        if short_code == "si":
            print("Sign in")
            print("Enter your desired user name")
            print("_" * 20)
            locker_userName = input()
            print("Choose a password")
            print("_" * 20)
            locker_password = input()
            save_user(create_user(locker_userName, locker_password))
            print("Keep your password to your self and out of reach")
            print("")
            print(f"""Your user details - {locker_userName}
                    {locker_password}""")
            print("")

        elif short_code == "lg":
            print("Log in")
            print("Enter User Name")
            print("_" * 20)
            locker_userName = input()
            print("Enter password")
            print("_" * 20)
            locker_password = input()

        print(f"Hi {locker_userName}! What would you like to do?")
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
                                print(
                                    f"{password.account_name} {password.user_name} {password.email} {password.account_password}")
                                print("")
                    else:
                            print("")
                            print("You dont seem to have any accounts saved yet")
                            print("")

            elif short_code == "fa":
                        print("Enter Account you want to search for")

                        search_account_name = input()
                        if checking_existing_passwords(search_account_name):
                            search_password = find_password(search_account_name)
                            print("_" * 20)
                            print(f"{search_password.account_name} {search_password.user_name}")
                            print("_" * 20)
                            print(f"Email Address - {search_password.email} ")
                            print("Account Password -{search_password.account_password}")
                            print("")

                        else:
                            print("That account does not exist")
            elif short_code == "ex":
                        print("Bye!! Thank you for using Password locker ")
                        break
            else:
                    print("I really didnt get that. Please use short code below")
                    print("")


if __name__=='__main__':
    main()
