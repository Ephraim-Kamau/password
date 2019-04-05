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
