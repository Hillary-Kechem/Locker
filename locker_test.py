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