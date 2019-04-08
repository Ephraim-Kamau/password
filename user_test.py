import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours
    '''

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

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
        self.assertEqual(self.new_user.user1, "Kamash")
        self.assertEqual(self.new_user.password, "password")

    def test_save_user(self):
        '''
        test_save_user test case  to test if the user object is saved into the user user_list
        '''
        self.new_user.save_user() #saving the new user
        self.assertEqual(len(User.user_list), 1)

    def test_save_multiple_users(self):
        '''
        test_save_multiple_users to check if we can save multiple users to out users list
        '''
        self.new_user.save_user()
        test_user = User("Winnie","Kimani", "winniek@moringa.com", "winniekim") #new users
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)

    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove users from our users_list
        '''
        self.new_user.save_user()
        test_user = User("Winnie","Kimani", "winniek@moringa.com", "winniekim") #new credentials for an account
        test_user.save_user()

        self.new_user.delete_user() #Deleting users
        self.assertEqual(len(User.user_list), 1)

    def test_user_exists(self):
        '''
        test to check if we can return a boolean if we cannot find the contact
        '''
        self.new_user.save_user()
        test_user = User("Test", "user", "test@moringa.com", "testpassword") #new contact
        test_user.save_user()

        user_exists = User.user_exist("Test")
        self.assertTrue(user_exists)

    def test_display_all_users(self):
        '''
        method that returns a list of all the users
        '''
        self.assertEqual(User.display_user(), User.user_list)



if __name__ == '__main__':
   unittest.main()
