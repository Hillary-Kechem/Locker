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
    Function to display all saved accounts
    '''
    return Credentials.display_accounts()

def delete_account(accountName):
    '''
    Function that deletes an account
    '''
    return Credentials.delete_account(accountName)

def main():
    print("Hello! Welcome to Locker, your ultimate security.")
    print('\n')

    while True:
        print('What would you like to do today?')
        print('use this short codes: su - signup, li - login in')
        start= input()
        if start =='su':
            print('Please enter your first name')
            first_name= input()
            print('please enter last name')

            print('Please enter your username')
            username = input()
            print('Enter password')
            password = input()
            print('Please confirm password')
            password = input()
            print('Signed up succesfully')
        elif start == 'li':
            print('Please enter your profile username')
            username = input()
            print('Enter Password')
            password = input()
            print('You are now logged in')
        else:
            print('I dont understand you, please use code above')
