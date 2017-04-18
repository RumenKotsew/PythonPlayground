class Flight():
    def __init__(self, passengers, max_passengers,
                 from_dest, to_dest, terminal, declined, start_time, end_time):
        self.passengers = passengers
        self.max_passengers = max_passengers
        self.from_dest = from_dest
        self.to_dest = to_dest
        self.terminal = terminal
        self.declined = declined
        self.start_time = start_time
        self.end_time = end_time

    def flight_duration(self):
        return self.end_time - self.start_time

    def flight_empty_seats(self):
        return self.max_passengers - self._get_passenger_count()

    def _get_passenger_count(self):
        res = 0
        for item in self.passengers:
            res += 1
        return res

    def passengers_under_18(self, flight):
        res = 0
        for k, v in self.passengers.items():
            for inner_k, inner_v in v:
                if inner_k == 'age' and inner_v < 18:
                    res += 1
        return res
