import re
from database.modify_database import *
from database.create_database import *
from interface import *
from decorators import *
from settings import *


def validate_username(username):
    users = get_users()
    users = [user['username'] for user in users]

    if username in users:
        username = input("Username exists. Enter new username: ")

    return username


def validate_pass(pword):
    if re.search(r'[A-Z]', pword) and re.search(r'[^0-9A-Za-z]', pword) and len(pword) > 7:
        return True
    return False


def check_user(username):
    users = get_users()
    usernames = [person['username'] for person in users]

    if username not in usernames:
        print("User not registered!")
        user = input("Enter a username: ")
        password = input("Enter a password: ")
        new_user = User(user, password)
        insert_user(new_user)

    return username


def check_login(username, password):
    users = get_users()
    pword = [person['password'] for person in users if person['username'] == username][0]
    while decorators.password.encode_pass(password) != decorators.password.encode_pass(pword):
        password = input("Incorrect password! Enter again: ")
    login(username)

    return username
