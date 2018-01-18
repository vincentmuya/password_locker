class Password:
    '''
    class that generates new instances of Passwords
    '''
    password_list =[] #Empty password_list

    def __init__(self,account_name,user_name,account_password):
        '''
        __init__method that helps us define properties for our object
        '''

        self.account_name = account_name
        self.user_name = user_name
        self.account_password = account_password
