import unittest
from password_locker import Password

class TestPassword(unittest.TestCase):

    def setUp(self):

        self.new_password = Password("Facebook","Vincent Muya","fb12345")

    def test_init(self):

        self.assertEqual(self.new_password.account_name,"Facebook")
        self.assertEqual(self.new_password.user_name,"Vincent Muya")
        self.assertEqual(self.new_password.account_password,"fb12345")
    def test_save_password(self):
        self.new_password.save_password()
        self.assertEqual(len(Password.password_list),1)

if __name__=='__main__':
    unittest.main()
