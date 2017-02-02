class Terminal():
    def __init__(self, number, max_flights):
        self.number = number
        self.max_flights = max_flights
        self.flights = []

    def _search_flights_for(self, search_clause, target):
        res = []
        for flight in self.flights:
            for k, v in flight.items():
                if k == str(search_clause) and v == target:
                    res.append(flight)
        return res

    def get_flights_for(self, date):
        return self._search_flights_for('start_time', date)

    def terminal_flights_to_dest(self, destination):
        return self._search_flights_for('to_dest', destination)

    def flights_on_date_lt_hours(self, date, hours):
        pass

    def flights_within_duration(self, start_time, end_time):
        pass

    def get_flight_before(self, date, hour):
        pass

    def get_terminal_flights(self):
        pass

    def get_terminal_flights_on(self, date):
        pass

    def get_flight_from(self, destination):
        pass

    def get_flight_to(self, destination):
        pass

    def get_specific_flight_to(self, destination, date, hour):
        pass

    def get_specific_flight_from(self, destination, date, hour):
        pass

    def reservations_to_destination(self, destination):
        pass

    def passengers_to_dest(self, destination):
        pass

    def flights_with_passengers(self, size):
        pass

    def passengers_from_terminal(self, terminal):
        pass

    def passengers_reservations(self, flight):
        pass
