class User:
    '''
    Class that generates new instances of users
    '''

    user_list = [] #empty user list

    def __init__(self, first_name, last_name, email_address, password):
        '''
        __init__ method that helps us define properties for our users
        '''
        self.first_name = first_name
        self.last_name = last_name
        self. email_address = email_address
        self.password = password

    def save_user(self):
        '''
        save_user method saves user into user_list
        '''
        User.user_list.append(self)

    def delete_user(self):
            '''
            delete_user method deletes  a saved user from the user_list
            '''
            User.user_list.remove(self)

    @classmethod
    def user_exist(cls,first_name):
        '''
        Method that checks if a user exists from the user list
        Args:
        name: first_name to search if it exists
        Returns:
        Boolean: true or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.first_name == first_name:
                return True

        return False

    @classmethod
    def display_user(cls):
        '''
        method that returns a list of all the users saved
        '''
        return cls.user_list
