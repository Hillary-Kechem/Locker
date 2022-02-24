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

    #######


def create_account(accountName,accountUsername, accountPassword):
    '''function to create new account
    '''
    new_account=Credentials(accountName,accountUsername, accountPassword)
    return new_account

def save_account(account):
    '''
    function to save account
    '''
    account.save_account


def find_account(accountUsername):
    '''
    Function that find an account by username
    '''
    return Credentials.find_by_accountUsername(accountUsername)

def check_existing_account(accountUsername):
    '''
    Function to check all the saved account
    '''
    return Credentials.account_exist(accountUsername)

def display_accounts():
    '''
    Function that returns all saved accounts
    '''
    return Credentials.display_accounts()




