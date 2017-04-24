from controllers import get_all_teams
from prettytable import PrettyTable
from datetime import datetime, timedelta


def convert_time(time_value):
    needed_time = str(time_value).split(' ')[1].split(':')
    res = needed_time[0] + ':' + needed_time[1]
    return res


def compose_schedule():
    table = PrettyTable(['Hour', 'Team', 'Idea'])
    table.padding_width = 1
    date = datetime.now()
    table.add_row([convert_time(date), 'Откриване', 'Откриване на хакатона'])
    for team in get_all_teams():
        table.add_row([convert_time(date + timedelta(minutes=15)), team[0], team[1]])
        date += timedelta(minutes=15)
    return table


def main():
    print(compose_schedule())


if __name__ == '__main__':
    main()
