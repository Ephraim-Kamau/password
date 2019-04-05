import unittest #Importing the unittest module
from credentials import Credentials #Importing the User class

class TestUser(unittest.TestCase):

    '''
    Test case that defines test cases for the user class behaviours
    Args:
    unittest.TestCase: TestCase class that helps in creating test classes
    '''
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

if __name__ == '__main__':
    unittest.main()
