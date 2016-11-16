from unittest import TestCase, main
from airlines import Date
from airlines import Terminal
from airlines import Flight
from airlines import Passenger


class TestDate(TestCase):  # done
    def setUp(self):
        self.custom_day = 29
        self.custom_month = 10
        self.custom_year = 2015
        self.custom_hour = '15:30'
        self.date = Date(self.custom_day, self.custom_month,
                         self.custom_year, self.custom_hour)


class TestFlight(TestCase):  # done
    def setUp(self):
        self.custom_passengers = 100
        self.custom_max_passengers = 150
        self.custom_from_dest = 'Sofia'
        self.custom_to_dest = 'Milano'
        self.custom_terminal = Terminal(2, 30)
        self.custom_declined = False
        self.custom_start_time = Date(29, 10, 2012, hour='12:20')
        self.custom_end_time = Date(29, 10, 2012, hour='17:30')
        self.flight = Flight(self.custom_start_time,
                             self.custom_end_time, self.custom_passengers,
                             self.custom_max_passengers, self.custom_from_dest,
                             self.custom_to_dest, self.custom_terminal,
                             self.custom_declined)

    def test_flight_duration(self):
        custom_duration = self.flight.duration_parser(
            self.custom_start_time, self.custom_end_time)
        self.assertEqual(custom_duration, '05:10')

    def test_duration_parser(self):
        self.test_result = self.custom_start_time.duration_parser(
            self.custom_start_time, self.custom_end_time)
        self.assertEqual(test_result, '05:10')

    def test_flight_empty_seats(self):
        self.assertEqual(self.flight.flight_empty_seats(), 50)

    def test_passengers_under_18(self):
        self.assertEqual(flight.passengers_under_18(), 0)


class TestTerminal(TestCase):
    def setUp(self):
        self.custom_number = 5
        self.custom_max_flights = 20
        self.terminal = Terminal(self.custom_number, self.custom_max_flights)
        self.flights = []

    def test_get_flights_for(self):
        self.custom_date = Date(29, 10, 2010, hour='22:20')
        self.assertEqual(self.terminal.get_flights_for(self.custom_date), 0)

    def test_terminal_flights_to_dest(destination):
        pass

    def test_flights_on_date_lt_hours(date, hours):
        pass

    def test_flights_within_duration(start_time, end_time):
        pass

    def test_get_flight_before(date, hour):
        pass

    def test_get_terminal_flights():
        pass

    def test_get_terminal_flights_on(date):
        pass

    def test_get_flight_from(destination):
        pass

    def test_get_flight_to(destination):
        pass

    def test_get_specific_flight_to(destination, date, hour):
        pass

    def test_get_specific_flight_from(destination, date, hour):
        pass

    def test_reservations_to_destination(destination):
        pass

    def test_passengers_to_dest(destination):
        pass

    def test_flights_with_passengers(size):
        pass

    def test_passengers_from_terminal(terminal):
        pass

    def test_passengers_reservations(flight):
        pass


class TestPassenger(TestCase):  # done
    def setUp(self):
        self.custom_first_name = "Rositsa"
        self.custom_last_name = "Zlateva"
        self.custom_flight = Flight(start_time=Date(29, 10, 2010,
                                                    hour='15:15'),
                                    end_time=Date(29, 10, 2010,
                                                  hour='20:30'),
                                    passengers=100, max_passengers=120,
                                    from_dest='Sofia', to_dest='Moscow',
                                    terminal=Terminal(2, 30), declined=False)
        self.custom_age = 22
        self.passenger = Passenger(self.custom_first_name,
                                   self.custom_last_name,
                                   self.custom_flight,
                                   self.custom_age)


class TestReservation(TestCase):  # done
    def setUp(self):
        self.custom_flight = Flight(start_time=Date(29, 10, 2010,
                                                    hour='15:15'),
                                    end_time=Date(29, 10, 2010,
                                                  hour='20:30'),
                                    passengers=100, max_passengers=120,
                                    from_dest='Sofia', to_dest='Moscow',
                                    terminal=Terminal(2, 30), declined=False)
        self.custom_passenger = Passenger(first_name='Rumen',
                                          last_name='Kotsev',
                                          self.custom_flight,
                                          age=22)
        self.custom_accepted = True
        self.reservation = Reservation(custom_flight, custom_passenger,
                                       custom_accepted)


class TestFlightsContainer(TestCase):  # done
    def setUp(self):
        self.custom_flights = []
        self.custom_max_flights = 150
        self.custom_flight = Flight(passengers=100, max_passengers=120,
                                    from_dest='Sofia', to_dest='London',
                                    terminal=Terminal(3, 50), declined=False,
                                    start_time=Date(5, 10, 2010, hour='12:40'),
                                    end_time=Date(5, 10, 2010, hour='16:20'))

    def test_append_flight(self):
        self.assertTrue(self.custom_flights.append_flight(self.custom_flight))

    def test_is_full(self):
        self.assertFalse(self.custom_flights.is_full())

    def test_get_size(self):
        self.assertEqual(len(self.custom_flights), 0)

    def test_flight_to_dict(self):
        self.custom_casted_result = \
            {'passengers': self.custom_flight.passengers,
             'max_passengers': self.custom_flight.max_passengers,
             'from_dest': self.custom_flight.from_dest,
             'to_dest': self.custom_flight.to_dest,
             'terminal': self.custom_flight.terminal,
             'declined': self.custom_flight.declined,
             'start_time': self.custom_flight.start_time,
             'end_time': self.custom_flight.end_time}
        self.assertEqual(self.custom_casted_result['passengers'], 100)
        self.assertEqual(self.custom_casted_result['max_passengers'], 120)
        self.assertEqual(self.custom_casted_result['from_dest'], 'Sofia')
        self.assertEqual(self.custom_casted_result['to_dest'], 'London')
        self.assertEqual(self.custom_casted_result['terminal'],
                         Terminal(3, 50))
        self.assertEqual(self.custom_casted_result['declined'], False)
        self.assertEqual(self.custom_casted_result['start_time'],
                         Date(5, 10, 2010, hour='12:40'))
        self.assertEqual(self.custom_casted_result['end_time'],
                         Date(5, 10, 2010, hour='16:20'))
