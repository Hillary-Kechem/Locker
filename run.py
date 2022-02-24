#!/usr/bin/env python3.6
from locker import Credentials
from locker import User

def create_user(username, password):
    ''' 
        Functiion to create a new user
    '''
    new_user=User(username, password)
    return new_user

def save_user(user):
    '''
        save user data
    '''
    user.save_user()

    #########


