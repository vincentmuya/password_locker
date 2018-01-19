import unittest
from password import Password

class TestPassword(unittest.TestCase):

    def setUp():

        self.new_password = Password("Facebook","Vincent Muya","fb12345") 

    def test_init(self):

        self.assertEqual(self.new_password.account_name,"Facebook")
        self.assertEqual(self.new_password.user_name,"Vincent Muya")
        self.assertEqual(self.new_password.account_password,"fb12345")

if __name__=='__main__':
    unittest.main()
