import unittest #Importing the unittest module
from password import Password #importing the contact class module

class TestPassword(unittest.TestCase):
    '''
    Test class that defines test cases for the contact class behaviour
    '''
    def setUp():
        '''
        set up method to run each test cases
        '''
        self.new_password = Password("Facebook","Vincent Muya","fb12345") #create a password object

    def test_init(self):
        '''
        test_init test case to see of the objec is initialized properly
        '''
        self.assertEqual(self.new_password.account_name,"Facebook")
        self.assertEqual(self.new_password.user_name,"Vincent Muya")
        self.assertEqual(self.new_password.account_password)

if __name__=='__main__':
    unittest.main()
