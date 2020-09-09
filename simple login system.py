print('--------------------')

users = {}
status = ""

def displayMenu():
    status = input("are you a registered user [y for yes n for no]? Press q to quit:\n ")
    if status == "y":
        olduser()
    elif status == "n":
        newuser()


def newuser():
    createlogin = input("create login name:\n ")

    if createlogin in users:
        print("\nLogin name already exists\n")
    else:
        createpassword = input("create password: ")
        users[createlogin] = createpassword
        print("\nUser created\n")


def olduser():
    login = input("enter login:\n ")
    password = input("enter password:\n ")

    if login in users and users[login] == password:
        print("\nlogin successful\n")
    else:
        print("\nUser doesn't exist or wrong password\n")

while status != "q":
    displayMenu()



