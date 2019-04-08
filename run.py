#!/usr/bin/env python3.6

from user import User
from credentials import Credentials
import random

def create_user(fname, lname, user1, password):
        '''
        Function to create new users
        '''
        new_user = User(fname, lname, user1, password)
        return new_user

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def find_user(first_name):
    '''
    Function that finds a contact by the first name and returns a boolean
    '''
    return User.find_user(first_name)

def check_existing_user(first_name):
    '''
    Function that checks if a contact exists with that first name and returns a Boolean
    '''
    return User.user_exist(first_name)

def display_user():
    '''
    Function that returns all the saved users
    '''
    return User.display_user()

# credentials
def create_credentials(platform, username, password1):
    '''
    Function to create new credentials
    '''
    new_credentials = Credentials(platform, username, password1)
    return new_credentials

def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()

def del_credentials(credentials):
    '''
    Function to delete credentials
    '''
    credentials.delete_credentials()

def find_credentials(user_name):
    '''
    Function that finds credentials by the user name and returns a boolean
    '''
    return Credentials.find_by_first_name(user_name)

def check_existing_credentials(user_name):
    '''
    Function that checks if a contact exists with the user name and returns a Boolean
    '''
    return Credentials.credentials_exist(user_name)

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()

def main():
    print("Hello. Welcome to your Password Locker. Please enter the following details:")
    print("First Name...")
    user_first_name = input()
    print("Last Name...")
    user_last_name = input()
    print("User Name...")
    user_user1 = input()
    print("Password...")
    user_password = input()

    print(f"Hello {user_first_name}. What would you like to do?")
    print("----------------------------------------------------------------")

    while True:
        print("Use these short codes: \n cu - Create a new user, du - Display users, \n fu - Find a user, cc - Create new credentials, \n delc - Delete credentials, fc - Find credentials, \n dc - Display credentials,  ex - Exit")
        print("----------------------------------------------------------------")
        short_code = input().lower()
        if short_code == 'cu':
            print("New User")
            print("-"*10)

            print("First Name...")
            first_name  = input()

            print("Last Name...")
            last_name = input()

            print("User name...")
            user1 = input()

            print("Password...")
            password = input()

            save_user(create_user(first_name, last_name, user1, password)) # create and save new user
            print('\n')
            print(f"New User, {first_name} {last_name} created")
            print("----------------------------------------------------------------")

        elif short_code == 'du':
            if display_user():
                print("Here is a list of all your users")
                print('\n')

                for user in display_user():
                    print(f"First Name:  {user.first_name} \nLast Name: {user.last_name} \nE-mail Address: {user.user1_address} \nPassword: {user.password}")

                print("----------------------------------------------------------------")
            else:
                print('\n')
                print("You don't seem to have any users saved yet")
                print("----------------------------------------------------------------")

        elif short_code == 'fu':
            print("Enter the first name you want to search for")

            search_first_name = input()
            if check_existing_user(search_first_name):
                search_user = find_user(search_first_name)
                print(f"{search_user.first_name} {search_user.last_name}")
                print('-' * 20)

                print(f"User name......{search_user.user1}")
                print(f"Password......{search_user.password}")
            else:
                print("that user does not exist")
                print("----------------------------------------------------------------")

#Credentials
        elif short_code == 'cc':
                print("New Credentials")
                print("-"*10)

                print("New Platform...")
                platform  = input()

                print("User Name...")
                user_name  = input()

                print("Password...")
                print("Would you like an auto-generated password?")
                print("y - Yes, n - No")
                decision = input().lower()
                if decision == 'y':
                    print("Password")
                    rands = "zxcvb123456nmasdfgh3214jkqwertyu789598"
                    password1 = "".join(random.choice(rands) for _ in range(8))

                    print('\n')
                    print(f"Your new password is {password1}.")

                elif decision == 'n':
                        print("Enter the password:")
                        password1 = input()

                save_credentials(create_credentials(platform, user_name, password1)) # create and save new credentials
                print('\n')
                print(f"New Credentials:\nPlatform:{platform}\nUsername:{user_name}")
                print("----------------------------------------------------------------")

        elif short_code == 'dc':
            if display_credentials():
                print("Here is a list of all your credentials")
                print("----------------------------------------------------------------")

                for credentials in display_credentials():
                    print(f"Platform: {credentials.platform} \nUsername: {credentials.user_name} \nPassword: {credentials.password1}")

                print("----------------------------------------------------------------")
            else:
                print('\n')
                print("You don't seem to have any credentials saved yet")
                print("----------------------------------------------------------------")


        elif short_code == 'delc':
            print("Enter the platform name of the credentials you want to delete")
            delete_platform = input()
            check_existing_credentials(delete_platform)
            search_credentials = find_credentials(platform, delete_platform)
            print(f"Are you sure you want to delete the {search_credentials.platform} credentials?")

            print('\n')
            print("y - Yes, n - No")
            print('\n')
            decision = input().ascii_lower()
            if decision == 'y':fri
            delete_credentials(search_credentials)
            print('\n')
            print(f"{search_credentials.platform} credentials have been deleted"    )
            print('\n')
            #    else:
                #    print('\n')
                #    print("Credentials have not been deleted and are still available")
                #    print('\n')

        #    else:
            #    print('\n')
            #    print("The credential doesn't exist")
            #    print('\n')

        elif short_code == 'fc':
            print("Enter the user name you want to search for")

            search_user_name = input()
            if check_existing_credentials(search_user_name):
                search_credentials = find_credentials(search_user_name)
                print(f"{search_credentials.platform} {search_credentials.user_name}")
                print('-' * 20)

                print(f"Password......{search_credentials.password1}")
            else:
                print("Those credentials do not exist")
                print("----------------------------------------------------------------")

        elif short_code == 'ex':
            print("Bye....")

            break

        else:
            print("I really didn't get that. Please use the collowing short codes\n----------------------------------------------------------------")

if __name__ == '__main__':
    main()
