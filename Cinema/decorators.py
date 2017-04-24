from settings import DB_NAME
from database.manage_db_queries import *
from database.modify_database import *
from validators import *
from interface import *

import hashlib
import sqlite3
from datetime import datetime
from functools import wraps


db = sqlite3.connect(DB_NAME)
db.row_factory = sqlite3.Row
c = db.cursor()


def atomic(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            return res
        except Exception as e:
            db.rollback()
            print(e.with_traceback)
    return inner


def log_info(func):
    def inner(*args, **kwargs):
        with open("log_info.txt", 'a') as f:
            f.write("Reservation made on {}\n".format(str(datetime.now())))
        return func(*args, **kwargs)
    return inner


def encode_pass(pw):
    hash_object = hashlib.sha256(pw.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig


def validate_password(func):
    def inner(password):
        while validate_pass(password) is False:
            print("""
            Invalid password! Must be 8 symbols long, contain at least one
            special symbol, and have at least one capital letter!
            """)
            password = input("Enter new password: ")
        return func(password)
    return inner


def hash_password(func):
    def inner(password):
        password = encode_pass(password)
        return func(password)
    return inner


def user_exists(func):
    def inner(user, password):
        user_interface.validators.check_user(user)
        if logged(user):
            return func(user, password)
        user_interface.validators.check_login(user, password)
        return func(user, password)
    return inner
