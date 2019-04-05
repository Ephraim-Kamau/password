class Credentials:
    '''
    Class that generates new instances of credentials
    '''

    credentials_list = [] #empty user list

    def __init__(self, platform, user_name, password):
        '''
        __init__ method that helps us define properties for our users
        '''
        self.platform  = platform
        self.user_name = user_name
        self. password = password

    def save_credentials(self):
        '''
        save_credentials method saves user into credentials_list
        '''
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
        delete_credentials method deletes  a saved credential from the credentials_list
        '''
        Credentials.credentials_list.remove(self)

    @classmethod
    def credentials_exist(cls,user_name):
        '''
        Method that checks if a user exists from the credentials list
        Args:
        name: user name to search if it exists
        Returns:
        Boolean: true or false depending if the user exists
        '''
        for credentials in cls.credentials_list:
            if credentials.user_name == user_name:
                return True

        return False

    @classmethod
    def display_credentials(cls):
        '''
        method that returns a list of all the credentials saved
        '''
        return cls.credentials_list

#    def generate_password(size=10, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
#       """
#       generate_password helps in generating password for the user if the option is choosen

#       """
#       generated_pass = ''.join(random.choice(char)for _ in range(size))
#       return generated_password      
