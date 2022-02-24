#!/usr/bin/env python3.6
from locker import Credentials
from locker import User

def create_user(username, password):
    ''' 
    Functiion to create a new user
    '''
    new_user=User(username, password)
    return new_user