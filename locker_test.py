import unittest
from locker import Credentials
from locker import User

class TestUser(unittest.TestCase):
    '''Test class  for testing 
    '''
    def setUp(self):
        '''runs before each test case'''
        self.new_user = User('Kechem','password')
    
    def test__init(self):
        '''object initiated properly'''
        self.assertEqual(self.new_user.username, 'Kechem')
        self.assertEqual(self.new_user.password, 'password')


class TestCredentials(unittest.TestCase):
    '''Test class for testing creditials'''
    def setUp(self):
        '''runs before each test case'''
        self.new_credentials = Credentials('twiiter','beliot','pass')

    def test_save_account(self):
        '''see if it saves account'''
        self.new_account.save_account()
        self.assertEqual(len(Credentials.credentials_list),1)

    def tearDown(self):
        '''cleans up code'''
        Credentials.credentials_list=[]

    def test_save_multiple_account(self):
        '''see if it saves multiple accounts'''
        self.new_account.save_account()
        test_account = Credentials('twiiter','beliot','pass')
        test_account.save_account()
        self.assertEqual(len(Credentials.credentials_list),2)
    
    def test_delete_account(self):
        '''see if it deletes accounts'''
        self.new_account.save_account()
        test_account = Credentials('twiiter','beliot','pass')
        test_account.save_account()
        self.new_account.delete_account()
        self.assertEqual(len(Credentials.credentials_list,1))

    def test_find_account_by_username(self):
        '''Test to find a account by username'''
        self.new_account.save_account()
        test_account = Credentials('twiiter','beliot','pass')
        test_account.save_account()
        find_account= Credentials.find_accountUsername('beliot')
        self.assertEqual(find_account.accountUsername,test_account.accountUsername)

    def test_account_exists(self):
        '''Test account to see if account exists'''
        self.new_account.save_account()
        test_account = Credentials('twiiter','beliot','pass')
        test_account.save_account()

        account_exists = Credentials.account_exists('beliot')
        self.assertTrue(account_exists)

    def test_display_all_accounts(self):
        '''Test to display all accounts'''
        self.assertEqual(Credentials.display_account(),Credentials.credentials_list)

    if __name__ == '__main__':
        unittest.main()



