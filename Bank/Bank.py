# Main program for controlling a Bank made up of Accounts
from bank6 import *

# Create an instance of the Bank
oBank = Bank('9 to 5', '123 Main Street, Anytown, USA', '(650) 555-1212')

# Main code
while True:
    print()
    print('To get an account balance, press b')
    print('To close an account, press c')
    print('To make a deposit, press d')
    print('To get bank information, press i')
    print('To open a new account, press o')
    print('To quit, press q')
    print('To show all accounts, press s')
    print('To make a withdrawal, press w')
    print()

    action = input('What do you want to do? ').lower()

    action = action[0]
    print()

    try:
        if action == 'b':
            oBank.balance()

        if action == 'c':
            oBank.closeAccount()

        if action == 'd':
            oBank.deposit()

        if action == 'i':
            oBank.getInfo()

        if action == 'o':
            oBank.openAccount()

        if action == 's':
            oBank.show()

        if action == 'q':
            break

        if action == 'w':
            oBank.withdraw()

    except AbortTransaction as error:
        print('error')

print('Done')
