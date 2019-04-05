import unittest #Importing the unittest module
from credentials import Credentials #Importing the User class

class TestCredentials(unittest.TestCase):

    '''
    Test case that defines test cases for the user class behaviours
    Args:
    unittest.TestCase: TestCase class that helps in creating test classes
    '''

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []

    def setUp(self):
        '''
        test_init test case to test  if the object is initialized properly
        '''
        self.new_credentials = Credentials("Twitter", "Ephraim1", "password1")

    def test_init(self):
        '''
        test_init test case to test if th eobject is initialized properly
        '''
        self.assertEqual(self.new_credentials.platform, "Twitter")
        self.assertEqual(self.new_credentials.user_name, "Ephraim1")
        self.assertEqual(self.new_credentials.password, "password1")

    def test_save_credentials(self):
        '''
        test_save_credentials test case  to test if the user object is saved into the credentials_list
        '''
        self.new_credentials.save_credentials() #saving the new credentials
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_credentials to check if we can save multiple credentials to out credentials list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Facebook","Ephraim2", "facebook2") #new credentials for an account
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 2)

if __name__ == '__main__':
    unittest.main()
