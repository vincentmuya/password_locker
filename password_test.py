import pyperclip
import unittest # Importing the unittest module
from password_locker import Password  # Importing the contact class

class TestPassword(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''

        self.new_password = Password("Facebook","Vincent Muya","vincentmuya13@gmail.com","fb12345") # create password object

    def tearDown(self):

        Password.password_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_password.account_name,"Facebook")
        self.assertEqual(self.new_password.user_name,"Vincent Muya")
        self.assertEqual(self.new_password.email,"vincentmuya13@gmail.com")
        self.assertEqual(self.new_password.account_password,"fb12345")
    def test_save_password(self):
        self.new_password.save_password()
        self.assertEqual(len(Password.password_list),1)

    def test_save_multiple_password(self):
        self.new_password.save_password()
        test_password = Password("Test","user","vincentmuya13@gmail.com","test12345")
        test_password.save_password()
        self.assertEqual(len(Password.password_list),2)

    def test_delete_password(self):
        self.new_password.save_password()
        test_password = Password("Test","user","vincentmuya13@gmail.com","test12345")
        test_password.save_password()
        self.new_password.delete_password()
        self.assertEqual(len(Password.password_list),1)

    def test_find_password_by_account_name(self):
        self.new_password.save_password()
        test_password = Password("Test","user","vincentmuya13@gmail.com","test12345")
        test_password.save_password()
        found_password = Password.find_by_account_name("Test")
        self.assertEqual(found_password.account_password,test_password.account_password)

    def test_password_exists(self):
        self.new_password.save_password()
        test_password = Password("Test","user","vincentmuya13@gmail.com","test12345")
        test_password.save_password()
        password_exists = Password.password_exist("user")
        self.assertTrue(password_exists)

    def test_display_all_passwords(self):
        self.assertEqual(Password.display_passwords(),Password.password_list)

if __name__=='__main__':
    unittest.main()
