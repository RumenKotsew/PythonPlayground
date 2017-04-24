import sql_manager
from exceptions import PasswordNotStrongEnoughException, UserAndPasswordDontMatchException
import getpass
from time import sleep


counter = 0


# USE DATETIME IN DATABASE
def main_menu():
    global counter
    print("Welcome to our bank service. You are not logged in. \nPlease register or login")
    while True:
        command = input("$$$>")
        if command == 'register':
            username = input("Enter your username: ")
            password = getpass.getpass("Enter your password: ")
            try:
                sql_manager.register(username=username, password=password)
            except PasswordNotStrongEnoughException:
                print("Password must contain at least one number, one uppercase and lowercase letter and a total length of at least six symbols!")
                return main_menu()
            print("Registration Successful")

        elif command == 'login':
            username = input("Enter your username: ")
            password = getpass.getpass("Enter your password: ")
            try:
                logged_user = sql_manager.login(username=username, password=password)
            except UserAndPasswordDontMatchException:
                print("User and password dont match!")
                return main_menu()
            if logged_user:
                counter = 0
                logged_menu(logged_user)
            else:
                print("Login failed")

        elif command == 'help':
            print("login - for logging in!")
            print("register - for creating new account!")
            print("exit - for closing program!")

        elif command == 'exit':
            break
        else:
            print("Not a valid command")


def logged_menu(logged_user):
    print("Welcome you are logged in as: " + logged_user.get_username())
    while True:
        command = input("Logged>>")

        if command == 'info':
            print("You are: " + logged_user.get_username())
            print("Your id is: " + str(logged_user.get_id()))
            print("Your balance is:" + str(logged_user.get_balance()) + '$')

        elif command == 'changepass':
            new_pass = getpass.getpass("Enter your new password: ")
            sql_manager.change_pass(new_pass, logged_user)

        elif command == 'change-message':
            new_message = input("Enter your new message: ")
            sql_manager.change_message(new_message, logged_user)

        elif command == 'show-message':
            print(logged_user.get_message())

        elif command == 'help':
            print("info - for showing account info")
            print("changepass - for changing passowrd")
            print("change-message - for changing users message")
            print("show-message - for showing users message")


def main():
    sql_manager.create_clients_table()
    main_menu()


if __name__ == '__main__':
    main()
