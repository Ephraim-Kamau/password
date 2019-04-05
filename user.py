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
