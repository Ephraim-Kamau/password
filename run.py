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
    print("Hello. Welcome to your Password Locker.")
    print("Enter your name")
    name = input()

    print(f"Hello {name}. What would you like to do?")
    print("----------------------------------------------------------------")

    while True:
        print("Use these short codes: \n cu - Create a new user, du - Display users, \n cc - Create new credentials, fc - Find Credentials \n  delc - Delete credentials,  dc - Display credentials,  ex - Exit")
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
                    print(f"First Name:  {user.first_name} \nLast Name: {user.last_name} \nUser name: {user.user1} \nPassword: {user.password}")

                print("----------------------------------------------------------------")
            else:
                print('\n')
                print("You don't seem to have any users saved yet")
                print("----------------------------------------------------------------")

#Credentials
        elif short_code == 'fc':
            print ('\n')
            print ('Enter the Platform you want to search for')
            search_platform = input()
            if check_existing_credentials(search_platform):
                search_credentials = find_credentials(search_platform)
                print('\n')
                print(f"Platform:{ search_credentials.platform}")
                print(f"User Name:{ search_credentials.account_user_name}")
                print(f"Password:{ search_credentials.account_password}")
                print ('\n')
            else:
                print('\n')
                print("That credential does not exist!")
                print('\n')

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

                for credential in display_credentials():
                    print(f"Platform: {credential.platform} \nUsername: {credential.user_name} \nPassword: {credential.password1}")

                print("----------------------------------------------------------------")
            else:
                print('\n')
                print("You don't seem to have any credentials saved yet")
                print("----------------------------------------------------------------")


        elif short_code == 'delc':
            print("Enter the platform name of the credentials you want to delete:")
            delete_credentials = input()
            if check_existing_credentials(delete_credentials):
                search_credentials = find_credentials(delete_credentials)
                print(f"Are you sure you want to delete the credentials?")
                print('\n')
                print("y - Yes, n - No")
                print('\n')
                decision = input().lower()
                if decision == 'y':
                    delete_credentials(search_credentials)
                    print('\n')
                    print("Credentials have been deleted")
                    print('\n')
                elif decision == 'n':
                        print('\n')
                        print("Credentials have not been deleted and are still available")
                        print('\n')

                else:
                   print('\n')
                   print("The credential doesn't exist")
                   print('\n')



        elif short_code == 'ex':
            print("Bye....")

            break

        else:
            print("I really didn't get that. Please use the collowing short codes\n----------------------------------------------------------------")

if __name__ == '__main__':
    main()
