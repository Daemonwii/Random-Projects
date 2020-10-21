import getpass,sys,time,functions
print_slow = functions.print_slow
class User:
    def __init__ (self, username, password, isAdmin, isLogged):
        self.username = username
        self.password = password
        self.isAdmin = isAdmin
        self.isLogged = isLogged
    def login(self):
        if self.isLogged == False:
            password_input = getpass.getpass('Password: ')
            if password_input == self.password:
                print 'You have logged in as',self.username
            else:
                print 'Incorrect password!'
        else:
            print 'You are already logged in!'
admin = User('admin','alpine',True,False)
johndoe = User('johndoe','password',False,False)
while True:
    try:
        username_input = input('Username: ')
        username_input.login()
        if username_input.isAdmin == True:
            print 'You have admin powers!'
        else:
            print 'You do not have admin powers!'
        break
    except:
        print 'Invalid username!'
while True:
    choice = raw_input('Do you wish to delete the entire registry? [y/n]: ')
    if choice == 'y' or choice == 'Y':
        if username_input.isAdmin == True:
            print_slow('Deleting the registry . . .')
        else:
            print_slow('You do not have admin privileges. HR will be notified of your actions. Good day.')
        break
    elif choice == 'n' or choice == 'N':
        print 'Not deleting the registry. Have a good day :)'
        break
    else:
        print 'That was not a valid option!'
