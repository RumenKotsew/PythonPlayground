import sqlite3
from sys import argv

from ..decorators import *

from settings import PROJECTIONS, DB_NAME, reservations

from manage_db_queries import *
from create_db_queries import INSERT_USERS, INSERT_RESERVATIONS


db = sqlite3.connect(DB_NAME)
db.row_factory = sqlite3.Row
c = db.cursor()


@atomic
def show_movies():
    c.execute(ORDER_BY_RATING)
    movies = c.fetchall()
    print('Current movies: ')
    for movie in range(len(movies)):
        print("[{}] - {} ({})".format(movie + 1, movies[movie]['name'],
                                      movies[movie]['rating']))


@atomic
def show_movie_projections(*args):
    if len(args) == 2:
        c.execute(ORDER_BY_DATE_AND_ID, (args[0], args[1]))
        projections = c.fetchall()
    elif len(argv) == 1:
        c.execute(ORDER_BY_ONLY_ID, (args[0], ))
        projections = c.fetchall()

    if len(args) == 2:
        print("Projections for movie '{}' on date {}:"
              .format(projections[0]['name'], args[1]))
        for projection in range(len(projections)):
            print("[{}] - {} ({}) - {} spots available"
                  .format(projections[projection]['id'],
                          projections[projection]['time_'],
                          projections[projection]['type'],
                          PROJECTIONS[projections[projection]['id'] - 1]
                          .free_seats()))
    elif len(args) == 1:
        print("Projections for movie '{}':".format(projections[0]['name']))
        for projection in projections:
            print("[{}] - {} ({}) - {} spots available"
                  .format(projection['id'],
                          projection['time_'],
                          projection['type'],
                          PROJECTIONS[projection['id'] - 1].free_seats()))


@atomic
def get_users():
    c.execute(SELECT_USERS)
    users = c.fetchall()
    return users


@atomic
def login(username):
    c.execute(SET_LOGGED, (username, ))
    db.commit()


@atomic
def logout(username):
    c.execute(SET_LOGOUT, (username, ))
    db.commit()


@atomic
def insert_user(user):
    c.execute(INSERT_USERS, (user.username, user.password))
    db.commit()
    login(user.username)


@atomic
def logged(username):
    c.execute(SELECT_LOGGED, (username, ))
    return c.fetchone()['logged'] == 1


@atomic
def insert_reservation(user, projection, row, col):
    c.execute(INSERT_RESERVATIONS, (user, projection, row, col))
    db.commit()


@atomic
def get_user_id(user):
    c.execute(SELECT_ID_BY_NAME, (user, ))
    return c.fetchone()['id']


@atomic
def get_movie_and_projection_info(movie_id, proj_id):
    c.execute(SELECT_MOVIE_PROJ_INFO, (movie_id, proj_id))
    return c.fetchone()


@atomic
def delete_reservations_by_name(username):
    c.execute(DELETE_RESERVATION, (username, ))
    db.commit()


def main():
    reservations()
    show_movie_projections()
    db.close()


if __name__ == '__main__':
    main()
