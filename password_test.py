import unittest
from password_locker import Password

class TestPassword(unittest.TestCase):

    def setUp(self):

        self.new_password = Password("Facebook","Vincent Muya","fb12345")

    def tearDown(self):

        Password.password_list = []

    def test_init(self):

        self.assertEqual(self.new_password.account_name,"Facebook")
        self.assertEqual(self.new_password.user_name,"Vincent Muya")
        self.assertEqual(self.new_password.account_password,"fb12345")
    def test_save_password(self):
        self.new_password.save_password()
        self.assertEqual(len(Password.password_list),1)

    def test_save_multiple_password(self):
        self.new_password.save_password()
        test_password = Password("Test","user","test12345")
        test_password.save_password()
        self.assertEqual(len(Password.password_list),2)

    def test_delete_password(self):
        self.new_password.save_password()
        test_password = Password("Test","user","test12345")
        test_password.save_password()
        self.new_password.delete_password()
        self.assertEqual(len(Password.password_list),1)

    def test_find_password_by_account_name(self):
        self.new_password.save_password()
        test_password = Password("Test","user","test12345")
        test_password.save_password()
        found_password = Password.find_by_account_name("Test")
        self.assertEqual(found_password.account_password,test_password.account_password)

if __name__=='__main__':
    unittest.main()
