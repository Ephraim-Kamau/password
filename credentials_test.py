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
        self.assertEqual(self.new_credentials.password1, "password1")

    def test_save_credentials(self):
        '''
        test_save_credentials test case  to test if the user object is saved into the credentials_list
        '''
        self.new_credentials.save_credentials() #saving the new credentials
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_credentials to check if we can save multiple credentials to our credentials list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Facebook","Ephraim2", "facebook2") #new credentials for an account
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 2)

    def test_delete_credentials(self):
        '''
        test_delete_credentials to test if we can remove credentials from our credentials_list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Facebook","Ephraim2", "facebook2") #new credentials for an account
        test_credentials.save_credentials()

        self.new_credentials.delete_credentials() #Deleting credentials
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_credentials_exists(self):
        '''
        test to check if we can return a boolean if we cannot find the credenetials
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Reddit", "AllBlacks", "redit3") #new credentials
        test_credentials.save_credentials()

        credentials_exists = Credentials.credentials_exist("AllBlacks")
        self.assertTrue(credentials_exists)

    def test_display_all_credentials(self):
        '''
        method that returns a list of all the credentials
        '''
        self.assertEqual(Credentials.display_credentials(), Credentials.credentials_list)
    

if __name__ == '__main__':
    unittest.main()
