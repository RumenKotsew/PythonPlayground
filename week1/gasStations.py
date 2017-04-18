def gas_stations(distance, tank_size, stations):
    stations.append(distance)
    return fill_list(tank_size, stations)


def fill_list(tank_size, stations):
    res = []
    current_stop = spend_tank(0, stations[1], tank_size, stations)
    while current_stop != len(stations) - 1:
        res.append(stations[current_stop])
        current_stop = spend_tank(current_stop,
                                  calc_km_to_next_stop(current_stop,
                                                       stations),
                                  tank_size, stations)
    return res


def spend_tank(current_stop, km_to_next_stop, tank, stations):
    if tank < km_to_next_stop or current_stop == len(stations) - 1:
        return current_stop
    else:
        tank -= km_to_next_stop
        return spend_tank(current_stop + 1,
                          calc_km_to_next_stop(current_stop, stations),
                          tank, stations)


def calc_km_to_next_stop(current_stop, stations):
    return stations[current_stop + 1] - stations[current_stop]
