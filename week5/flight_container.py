class FlightContainer():
    def __init__(self, max_flights):
        self.flights = []
        self.max_flights = max_flights

    def append_flight(self, new_flight):
        self.flights.append(self.flight_to_dict(new_flight))

    def is_full(self):
        return self.get_size() < self.max_flights

    def get_size(self):
        return len(self.flights)

    def flight_to_dict(self, new_flight):
        result = {'passengers': new_flight.passengers,
                  'max_passengers': new_flight.max_passengers,
                  'from_dest': new_flight.from_dest,
                  'to_dest': new_flight.to_dest,
                  'terminal': new_flight.terminal,
                  'declined': new_flight.declined,
                  'start_time': new_flight.start_time,
                  'end_time': new_flight.end_time}
        return result
