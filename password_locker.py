import pyperclip

import random
# global user_list
class User:

    user_list = []

    def __init__(self, locker_userName, locker_password):

        self.locker_userName = locker_userName
        self.locker_password = locker_password

    def save_user(self):
        User.user_list.append(self)

    # @classmethod
    # def find_by_account_name(cls, account_name)
    #     for user in cls.user_list:
    #         if user.locker_userName == account_name:
    #             return user


class Password:

    password_list =[]

    def __init__(self,account_name,user_name,email,account_password):


        self.account_name = account_name
        self.user_name = user_name
        self.email = email
        self.account_password = account_password

    def save_password(self):
        Password.password_list.append(self)

    def delete_password(self):
        Password.password_list.remove(self)

    @classmethod
    def find_by_account_name(cls,user_name):
            for password in cls.password_list:
                if password.user_name == user_name:
                    return password

    @classmethod
    def password_exist(cls,user_name):
        for password in cls.password_list:
            if password.user_name == user_name:
                return True
        return False

    @classmethod
    def display_passwords(cls):
        return cls.password_list

    @classmethod
    def copy_user_name(cls,user_name):
        password_found = Password.find_by_account_name(user_name)
        pyperclip.copy(password_found.account_password)
