import pyperclip
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
    def find_by_account_name(cls,account_name):
            for password in cls.password_list:
                if password.account_name == account_name:
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
