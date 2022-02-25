#!/usr/bin/env python3.8
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

        while True:
            print(f'Hello {username}. What would you like to do?')
            print("Use these short codes: ca - create a new account, da - display your saved accounts, fa - find an account, dlt - delete  account ex - exit the account ")
            
            short_code = input().lower()

            if short_code == 'ca':
                    print('New account')
                    print('-'*10)

                    print("Do you want to create an account?")
                    accountName = input()

                    print('Enter your username ...')
                    accountUsername = input()

                    print('Enter your Password ...')
                    accountPassword = input()

                    save_account(create_account(accountName, accountUsername, accountPassword))

                    print('\n')
                    print(f"New {accountName} account  with username {accountUsername} has been created successfully")
                    print('\n')

            elif short_code == 'da':

                    if display_accounts():
                        print("Below is a display of your accounts")
                        print('\n')

                        for account in display_accounts():
                            print(f"{account.accountName} {account.accountUsername}")
                            print('\n')
                    else:
                        print('\n')
                        print("We cant find your account")
                        print('\n')
                        
            elif short_code == 'fa':
                    print('Please search for your account')
                    search_accountUsername = input()
                    if check_existing_account(search_accountUsername):
                        search_account = find_account(search_accountUsername)
                        print(f"{search_account.accountName} {search_account.accountUsername} {search_account.accountPassword}")
                        print('-'*20)

                        print(f"Account name: {search_account.accountName}")
                        print(f"Account username: {search_account.accountUsername}")
                    else:
                        print("Ooop,we cant find your account")

            elif short_code == 'dlt':
                print('Please enter the account you want to delete')
                accountUsername = input()
                if find_account(accountUsername):
                    delete_account(find_account(accountUsername))
                    print(f'{accountUsername} has been deleted successfully')
                else:
                    print('The account does not exist')

            
            elif short_code == 'ex':
                print('Thank you and goodbye!!')
                break
            else:
                print('I really didnt get that. Please use the short codes')
