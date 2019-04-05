import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours
    '''

    def setUp(self):
        '''
        set up method to run before each test cases
        '''
        self.new_user = User("Ephraim", "Kamau", "kamau@moringa.com", "password")

    def test_init(self):
        '''
        test_init test case to test if the object is initializing properly
        '''
        self.assertEqual(self.new_user.first_name, "Ephraim")
        self.assertEqual(self.new_user.last_name, "Kamau")
        self.assertEqual(self.new_user.email_address, "kamau@moringa.com")
        self.assertEqual(self.new_user.password, "password")

    if __name__ == '__main__':
        unittest.main()
