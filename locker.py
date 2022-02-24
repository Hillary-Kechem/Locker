class User: 
# class user this is an instance of the user class
    '''
    This class generates instances for creating an user
    '''
    user_list=[]

    def __init__(self,username,password):
        '''
        this functon define the properties for creation of account
        
        Args:
            username: username
            password: password
        '''
        self.username = username
        self.password = password

    def save_user(self):
        '''
        Test to save new user
        '''
        User.user_list.apend(self)

    def delete_user(self):
        '''
        test to delete user
        '''



