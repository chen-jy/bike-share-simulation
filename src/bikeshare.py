"""Assignment 1 - Bike-share objects

=== CSC148 Fall 2017 ===
Diane Horton and David Liu
Department of Computer Science,
University of Toronto


=== Module Description ===

This file contains the Station and Ride classes, which store the data for the
objects in this simulation.

There is also an abstract Drawable class that is the superclass for both
Station and Ride. It enables the simulation to visualize these objects in
a graphical window.
"""
from datetime import datetime
from typing import Tuple


# Sprite files
STATION_SPRITE = 'stationsprite.png'
RIDE_SPRITE = 'bikesprite.png'


class Drawable:
    """A base class for objects that the graphical renderer can be drawn.

    === Public Attributes ===
    sprite:
        The filename of the image to be drawn for this object.
    """
    # Attribute types
    sprite: str

    def __init__(self, sprite_file: str) -> None:
        """Initialize this drawable object with the given sprite file.
        """
        self.sprite = sprite_file

    def get_position(self, time: datetime) -> Tuple[float, float]:
        """Return the (long, lat) position of this object at the given time.
        """
        raise NotImplementedError


class Station(Drawable):
    """A Bixi station.

    === Public Attributes ===
    capacity:
        the total number of bikes the station can store
    location:
        the location of the station in long/lat coordinates
        **UPDATED**: make sure the first coordinate is the longitude,
        and the second coordinate is the latitude.
    name: str
        name of the station
    num_bikes: int
        current number of bikes at the station
    rides_started: int
        The number of rides that started at the station during the simulation.
        Rides already in progress when the simulation begins are not counted.
    rides_ended: int
        The number of rides that ended at the station during the simulation.
        Rides that haven't ended when the simulation finishes are not counted.
    low_availability: int
        The total amount of time during the simulation, in seconds, that the
        station spent with at most five bikes available.
    low_unoccupied: int
        The total amount of time during the simulation, in seconds, that the
        station spent with at most five unoccupied spots.

    === Representation Invariants ===
    - 0 <= num_bikes <= capacity
    - rides_started >= 0
    - rides_ended >= 0
    - low_availability >= 0
    - low_unoccupied >= 0
    """
    # Attribute types
    name: str
    location: Tuple[float, float]
    capacity: int
    num_bikes: int
    rides_started: int
    rides_ended: int
    low_availability: int
    low_unoccupied: int

    def __init__(self, pos: Tuple[float, float], cap: int,
                 num_bikes: int, name: str) -> None:
        """Initialize a new station.

        Precondition: 0 <= num_bikes <= cap
        """
        Drawable.__init__(self, STATION_SPRITE)
        self.location = pos
        self.capacity = cap
        self.num_bikes = num_bikes
        self.name = name
        self.rides_started = 0
        self.rides_ended = 0
        self.low_availability = 0
        self.low_unoccupied = 0

    def get_position(self, time: datetime) -> Tuple[float, float]:
        """Return the (long, lat) position of this station for the given time.

        Note that the station's location does *not* change over time.
        The <time> parameter is included only because we should not change
        the header of an overridden method.
        """
        return self.location


class Ride(Drawable):
    """A ride using a Bixi bike.

    === Attributes ===
    start:
        the station where this ride starts
    end:
        the station where this ride ends
    start_time:
        the time this ride starts
    end_time:
        the time this ride ends

    === Representation Invariants ===
    - start_time < end_time
    """
    # Attribute types
    start: Station
    end: Station
    start_time: datetime
    end_time: datetime

    def __init__(self, start: Station, end: Station,
                 times: Tuple[datetime, datetime]) -> None:
        """Initialize a ride object with the given start and end information.
        """
        Drawable.__init__(self, RIDE_SPRITE)
        self.start, self.end = start, end
        self.start_time, self.end_time = times[0], times[1]

    def get_position(self, time: datetime) -> Tuple[float, float]:
        """Return the (long, lat) position of this ride for the given time.

        A ride travels in a straight line between its start and end stations
        at a constant speed.
        """
        # Get the known pieces of information
        start_pos = self.start.get_position(time)  # Pass time to satisfy
        end_pos = self.end.get_position(time)      # method signature
        total_time = (self.end_time - self.start_time).total_seconds()
        elapsed_time = (time - self.start_time).total_seconds()

        # Calculate the x- and y-components of speed
        vx = (end_pos[0] - start_pos[0]) / total_time
        vy = (end_pos[1] - start_pos[1]) / total_time
        # Calculate the current coordinates using the components of speed
        curr_x = start_pos[0] + elapsed_time * vx
        curr_y = start_pos[1] + elapsed_time * vy

        return (curr_x, curr_y)


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={
        'allowed-import-modules': [
            'doctest', 'python_ta', 'typing',
            'datetime'
        ],
        'max-attributes': 15
    })
