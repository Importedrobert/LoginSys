U = 'isaac'
P = 'isaac'

def menu():
    a = int(input('1. Login  2. Quit  <:'))
    if a == 1:
        return login()
    elif a == 2:
        return quit()
    else:
        return menu()

def login():
    global U 
    global P
    print('Please enter username and password.')
    u = input('Username: ')
    p = input('Password: ')
    if u == U and p == P:
        print('Logged in!')
        return menu2()
    elif u != U and p != P:
        print('Incorrect username/password. Please Try again')
        return login()

def menu2():
    print('ok it worked thank god')
    return menu()

def quit():
    print('Good-bye.')
    exit

menu()
