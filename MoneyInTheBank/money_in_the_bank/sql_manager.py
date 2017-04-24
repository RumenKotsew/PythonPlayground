import sqlite3
from datetime import datetime

from client import Client
from decorators.login import strong_password, hash_password
from exceptions import PasswordNotStrongEnoughException, UserAndPasswordDontMatchException

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()


def create_clients_table():
    create_query = '''create table if not exists
        clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                balance REAL DEFAULT 0,
                message TEXT,
                lastfailedloginattempt TEXT DEFAULT NULL,
                numberoftriesleft INTEGER)'''

    cursor.execute(create_query)


def change_message(new_message, logged_user):
    update_sql = "UPDATE clients SET message = '%s' WHERE id = '%s'" % (new_message, logged_user.get_id())
    cursor.execute(update_sql)
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    update_sql = "UPDATE clients SET password = '%s' WHERE id = '%s'" % (new_pass, logged_user.get_id())
    cursor.execute(update_sql)
    conn.commit()


@strong_password()
@hash_password()
def register(username, password):
    insert_sql = "insert into clients (username, password) values ('%s', '%s')" % (username, password)
    cursor.execute(insert_sql)
    conn.commit()


@hash_password()
def login(username, password):
    interval = 5 * 60

    select_query = "SELECT id, username, balance, message FROM clients WHERE username = '%s' AND password = '%s' LIMIT 1" % (username, password)

    time_query = "SELECT lastfailedloginattempt, numberoftriesleft FROM clients WHERE username = '%s" % (username)
    cursor.execute(select_query)
    user = cursor.fetchone()

    if user:
        time_counter_reset_query = "UPDATE numberoftriesleft VALUES(0) FROM clients WHERE id = '%s'" % (user.id)
        cursor.execute(time_counter_reset_query)
        cursor.commit()
        return Client(user[0], user[1], user[2], user[3])

    cursor.execute(time_query)
    user_time = cursor.fetchone()

    if not user_time:
        raise UserNotFoundException

    if user_time.lastfailedloginattempt is None:
        pass
    else:
        time = datetime.now()
        if time - user_time.lastfailedloginattempt < interval:
            user_time.numberoftriesleft += 1
            if user_time.numberoftriesleft == 5:
                raise BruteForceException
            else:
                increase_numbers_query = "UPDATE numberoftriesleft VALUES('%s') FROM clients WHERE id = '%s'" % (user_time.numberoftriesleft, user.id)
                cursor.execute(increase_numbers_query)
                cursor.commit()
