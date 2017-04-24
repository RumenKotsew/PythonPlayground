import sys
from decorators import *
from database.modify_database import *
from validators import *
from settings import *


@validate_password
@hash_password
def set_password(password):
    return password


def set_username(username):
    return validate_username(username)


class User:

    def __init__(self, username, password):
        self.username = set_username(username)
        self.password = set_password(password)

    def __str__(self):
        return "{} : {}".format(self.username, self.password)

    def __repr__(self):
        return self.__str__()


class Reservation:

    def __init__(self, user, projection, row, col):
        self.user = user
        self.projection = projection
        self.row = row
        self.col = col


class Projection:
    def __init__(self, proj_id):
        self.hall = np.array([["." for x in range(11)] for y in range(11)])
        number_row = ["-", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.hall[0] = number_row
        for row in range(1, 11):
            self.hall[row][0] = row - 1
        self.proj_id = proj_id

    def __str__(self):
        return "Here be a hall:\n{}".format(self.__print_matrix())

    def __print_matrix(self):
        return ('\n'.join([''.join(['{:2}'.format(item) for item in row]) for row in self.hall]))

    def __repr__(self):
        return self.__str__()

    def reserve_seat(self, row, col):
        if row == 0 or col == 0:
            raise IndexError
        self.hall[row][col] = 'x'
        return self.hall

    def free_seats(self):
        return (self.hall == '.').sum()

    def is_free_seat(self, seats):
        if seats[0] < 1 or seats[0] > 10 or seats[1] <= 0 or seats[0] > 10:
            return None
        return self.hall[seats[0]][seats[1]] != 'x'


@log_info
def finalize(user_id, projection_id, seats):
    for seat in seats:
        insert_reservation(user_id, projection_id, seat[0], seat[1])


@user_exists
def make_reservation(user, password=None):
    tickets = int(input("Choose number of tickets: "))
    show_movies()
    movie = input("Choose a movie: ")
    show_movie_projections(movie)
    projection = int(input("Choose a projection: "))
    proj = Projection(projection)
    proj.hall = PROJECTIONS[projection - 1].hall
    print("Available seats :")
    print(PROJECTIONS[projection - 1])
    chosen_seats = []
    for seat in range(tickets):
        seats = input("Choose seat {} :".format(seat + 1))
        seats = tuple(map(int, seats.split(',')))
        while proj.is_free_seat(seats) is None:
            print("Invalid seats - max seat is (10 10)")
            seats = input("Choose seat {} :".format(seat + 1))
            seats = tuple(map(int, seats.split(',')))
        while proj.is_free_seat(seats) is False:
            print("That seat is already taken!")
            seats = input("Choose seat {} :".format(seat + 1))
            seats = tuple(map(int, seats.split(',')))
        with open("settings", "a") as f:
            f.write("settings.PROJECTIONS[{}]. \
reserve_seat({}, {}) # by {}\n".format(projection - 1,
                                       seats[0], seats[1], user))
        chosen_seats.append(seats)
    print("This is your reservation: ")
    user_id = get_user_id(user)
    info = get_movie_and_projection_info(movie, projection)
    print("Movie: {} {}".format(info['name'], info['rating']))
    print("Profection: {} {} ({})".format(info['date_'],
                                          info['time_'],
                                          info['type']))
    print("Seats: {}".format(chosen_seats))
    end = input("Step 5 (Confirm - type 'done') :")
    while end != 'done':
        print("Type 'done' to finish your reservation.")
    finalize(user_id, projection, chosen_seats)
    logout(user)


def cancel_reservation(username):
    delete_reservations_by_name(username)
    with open('settings.py', 'w') as f:
        lines = f.readlines()
    print(lines)
    print('How many tickets do you want to cancel? ')
    tickets = input()
    lines = lines[::-1]
    for line in range(len(lines)):
        if username in lines[line]:
            for ticket in range(int(tickets)):
                lines.remove(lines[line])
            break
    lines = lines[::-1]
    f.write(line)


def exit():
    sys.exit()


def main_menu():
    print('Welcome to the cinema!')

    while True:
        print("""
              1 - show movies
              2 - show movie projections
              3 - make reservation
              4 - cancel reservation
              5 - exit
              """)
        print("Enter a command:")
        user_in = input()
        if user_in == '2':
            print('Enter movie id to see projections: ')
            movie = input()
            print("""Enter date(optional), \
                date must be in format yyyy-mm-dd.""")
            date = input()
            if date:
                show_movie_projections(movie, date)
            else:
                show_movie_projections(movie)
        elif user_in == '4':
            print('Enter username: ')
            username = input()
            cancel_reservation(user)
        elif user_in == '3':
            print('Enter username: ')
            username = input()
            print('Enter password: ')
            password = input()
            make_reservation(username, password)
        else:
            main_menu()


def main():
    main_menu()


if __name__ == '__main__':
    main()
