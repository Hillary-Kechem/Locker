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
        self.new_credentials = Credentials('twiiter','beliot','password')

    def test_save_account(self):
        '''see if it saves account'''
        self.new_account.save_account()
        self.assertEqual(len(Credentials.credentials_list),1)
        
