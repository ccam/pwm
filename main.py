#! /usr/bin/python3

'''

****************DISCLAIMER**********************
I am learning python, best programming practices, and do not know the best security measures to store passwords.
I made the program as a learning experience if it doesn't follow the best security standards please enlighten me.
Do not trust this program to securely store your information!!!!!!!!!!


------ pwm ------
password manager: This program creates strong passwords. stores the username, password, service combination and encrypts all of them.

TODO:
1) Add Delete password funtion
2) Fix 'enpw ref before declared' bug'
3) Finish ViewPassword()
4) Incorporate tkinter?

'''
import random, bcrypt, sqlite3
import os

print('''
        ________  _  _______  
        \____ \ \/ \/ /     \ 
        |  |_> >     /  Y Y  \  
        |   __/ \/\_/|__|_|  /
        |__|               \/ 
            Password Manager
''')


def MainMenu():
    MasterCheck()

    mainMenu = input('''
    Main Menu:
        1: Create Password
        2: View Stored Passwords
        3: Store New Password
        4: Exit
    ''')

    if mainMenu == '1':
        MakeNewPass.makePass()

    elif mainMenu == '2':
        ViewPasswords()

    elif mainMenu == '3':
        StoreNewPassword()

    elif mainMenu == '4':
        print('Thanks for using pwm!')
        return
    else:
        print('Not a choice Try again')
        MainMenu()


def MasterCheck():
    # function to check for master password
    # may not be needed once I know more about sqlite and working with databases

    # checks to see if 'data/db.sqlite is there and if not then creates it.
    dbFile = 'db.sqlite'
    dbFilePath = os.path.exists('data')
    if dbFilePath is True:
        if dbFile is True:
           os.path.isfile('data/'+dbFile)
        else:
            open('data/db.sqlite', 'a').close()
    else:
        os.makedirs('data')
        open('data/db.sqlite', 'a').close()

    # make master pw check

    '''
    db = sqlite3.connect('data/db')
    cursor = db.cursor()
    cursor.execute('''
        # CREATE TABLE users(if INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT unique, password TEXT)
    ''')

    db.close()
    '''

class MakeNewPass():

    def makePass(self):
        passlen = input('How long does the password need to be? 8+ ')

        if passlen == '' or passlen < 8:
            passlen = 8

        s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
        p = "".join(random.sample(s, passlen))
        print('Your new password is: ' + p)
        return p



def ViewPasswords():
    print('view')


def StoreNewPassword():
    print('store')


MainMenu()
