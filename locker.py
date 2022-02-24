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
# class user this is an instance of the credentials class
class Credentials:
    '''
    this enerates instances of new accounts
    '''
    credentials_list=[]

    def __init__(self,accountName, accountUsername, accountPassword):
        '''
        this function defines account objects

        Args: 
            accountName: 'twiiter'
            accountUsername: 'beliot'
            accountPassword: 'password'
        '''

        self.accountName:accountName
        self.accountUsername:accountUsername
        self.accountPassword:accountPassword

    def save_account(self):
        '''
        saves details of account
        '''
        Credentials.credentials_list.append(self) 

    def delete_account(self):
        '''
        this deletes details of account
        '''
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_accountUsername(cls, accountUsername):
        '''
        method to check username
        '''
        for account in cls.credentials_list:
            if account.accountUsername == accountUsername:
                return account
                

