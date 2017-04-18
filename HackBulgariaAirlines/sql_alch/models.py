from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()


class Terminal(Base):
    __tablename__ = 'Terminal'
    id = Column(Integer, primary_key=True)
    max_flights = Column(Integer)


class Flight(Base):
    __tablename__ = 'Flight'
    id = Column(Integer, primary_key=True)
    from_dest = Column(String)
    to_dest = Column(String)
    terminal = Column(Integer, ForeignKey('Terminal.id'))
    declined = Column(Boolean)
    start_time = Column(String)
    end_time = Column(String)


class Reservation(Base):
    __tablename__ = 'Reservation'
    id = Column(Integer, primary_key=True)
    accepted = Column(Boolean)


class Passenger(Base):
    __tablename__ = 'Passenger'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    flight = relationship(Flight, secondary=Reservation)
    age = Column(Integer)


def main():
    engine = create_engine('sqlite:///hack_flights.db', echo=True)
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    main()
