"""Assignment 1 - Simulation
=== CSC148 Fall 2017 ===
Diane Horton and David Liu
Department of Computer Science,
University of Toronto
=== Module Description ===
This file contains the Simulation class, which is the main class for your
bike-share simulation.
At the bottom of the file, there is a sample_simulation function that you
can use to try running the simulation at any time.
"""
import csv
from datetime import datetime, timedelta
import json
from typing import Dict, List, Tuple

from bikeshare import Ride, Station
from container import PriorityQueue
from visualizer import Visualizer

# Datetime format to parse the ride data
DATETIME_FORMAT = '%Y-%m-%d %H:%M'


class Simulation:
    """Runs the core of the simulation through time.
    === Attributes ===
    all_rides:
        A list of all the rides in this simulation.
        Note that not all rides might be used, depending on the timeframe
        when the simulation is run.
    all_stations:
        A dictionary containing all the stations in this simulation.
    visualizer:
        A helper class for visualizing the simulation.
    active_rides:
        A list of all the rides currently in progress in the simulation. Only
        these rides are visualized.
    start_time:
        The start time of the simulation. It is set to the current time when a
        Simulation is first created, but is set to the correct starting time
        when the Simulation is run. It allows Events to properly update station
        statistics.
    === Private Attributes ===
    _event_pq:
        A priority queue containing ride start and ride end events to process
        active rides more efficiently. Earlier events are extracted first.
    """
    # Attribute types
    all_stations: Dict[str, Station]
    all_rides: List[Ride]
    visualizer: Visualizer
    active_rides: List[Ride]
    start_time: datetime
    _event_pq: PriorityQueue['Event']

    def __init__(self, station_file: str, ride_file: str) -> None:
        """Initialize this simulation with the given configuration settings.
        """
        self.visualizer = Visualizer()
        self.all_stations = create_stations(station_file)
        self.all_rides = create_rides(ride_file, self.all_stations)
        self.active_rides = []
        self.start_time = None  # Will be set when the simulation is run
        self._event_pq = PriorityQueue()

    def run(self, start: datetime, end: datetime) -> None:
        """Run the simulation from <start> to <end>.
        """
        self.start_time = start

        step = timedelta(minutes=1)  # Each iteration spans one minute of time
        # List of stations; no need to cast the values every minute
        stations = list(self.all_stations.values())

        # Create the initial ride start events
        self._init_ride_start_events(start, end)

        # Main simulation loop
        curr_time = start
        while curr_time <= end:
            # self._update_active_rides(curr_time)
            self._update_active_rides_fast(curr_time)
            drawables = stations + self.active_rides
            self.visualizer.render_drawables(drawables, curr_time)

            # Make sure not to overcount statistics
            if curr_time < end or start == end:  # start == end is an edge case
                self._update_low_statistics()
            curr_time += step

        # Leave this code at the very bottom of this method.
        # It will keep the visualization window open until you close
        # it by pressing the 'X'.
        while True:
            if self.visualizer.handle_window_events():
                return  # Stop the simulation

    def _init_ride_start_events(self, start: datetime, end: datetime) -> None:
        """Create ride start events for all rides within the given time range.
        """
        for ride in self.all_rides:
            # Add the rides that start after the simulation's start time as well
            # as the rides that haven't ended yet.
            if ride.start_time <= end and ride.end_time >= start:
                self._event_pq.add(RideStartEvent(self, ride.start_time,
                                                  ride))

    def _update_active_rides(self, time: datetime) -> None:
        """Update this simulation's list of active rides for the given time.
        REQUIRED IMPLEMENTATION NOTES:
        -   Loop through `self.all_rides` and compare each Ride's start and
            end times with <time>.
            If <time> is between the ride's start and end times (inclusive),
            then add the ride to self.active_rides if it isn't already in
            that list.
            Otherwise, remove the ride from self.active_rides if it is in
            that list.
        -   This means that if a ride started before the simulation's time
            period but ends during or after the simulation's time period,
            it should still be added to self.active_rides.
        """
        for ride in self.all_rides:
            # If the ride can end
            if ride.end_time == time and ride.end.num_bikes < ride.end.capacity:
                if ride in self.active_rides:
                    self.active_rides.remove(ride)
                    ride.end.rides_ended += 1
                    ride.end.num_bikes += 1
                # Edge case: ride started before and ends at sim start
                elif ride.start_time < self.start_time:
                    ride.end.rides_ended += 1
                    ride.end.num_bikes += 1
                # Edge case: ride starts and ends at the same minute
                elif ride.start_time == time and ride.start.num_bikes > 0:
                    ride.start.rides_started += 1
                    ride.start.num_bikes -= 1
            # Ride can't end, so just unvisualize it
            elif ride in self.active_rides and ride.end_time == time:
                self.active_rides.remove(ride)

            # Ensure time is correct and there are enough bikes to start
            elif (ride.start_time <= time < ride.end_time and
                  ride not in self.active_rides and ride.start.num_bikes > 0):
                self.active_rides.append(ride)
                # Update station statistics only if the ride started after the
                # simulation's start time.
                if ride.start_time == time:
                    ride.start.rides_started += 1
                    ride.start.num_bikes -= 1

    def _update_low_statistics(self) -> None:
        """Update each station's low_availability and low_unoccupied statistics.
        Check to see if any station has at most five bikes available or at most
        five unoccupied spots, respectively.
        """
        for station in self.all_stations.values():
            if station.num_bikes <= 5:
                station.low_availability += 60  # Time in seconds
            if station.capacity - station.num_bikes <= 5:
                station.low_unoccupied += 60

    def calculate_statistics(self) -> Dict[str, Tuple[str, float]]:
        """Return a dictionary containing statistics for this simulation.
        The returned dictionary has exactly four keys, corresponding
        to the four statistics tracked for each station:
          - 'max_start'
          - 'max_end'
          - 'max_time_low_availability'
          - 'max_time_low_unoccupied'
        The corresponding value of each key is a tuple of two elements,
        where the first element is the name (NOT id) of the station that has
        the maximum value of the quantity specified by that key,
        and the second element is the value of that quantity.
        For example, the value corresponding to key 'max_start' should be the
        name of the station with the most number of rides started at that
        station, and the number of rides that started at that station.
        """
        # Default values guaranteed to be overwritten in the first loop
        max_start_val, max_start_name = -1, ''
        max_end_val, max_end_name = -1, ''
        max_low_avail_val, max_low_avail_name = -1, ''
        max_low_unocc_val, max_low_unocc_name = -1, ''

        # This is self-documenting code
        for station in self.all_stations.values():
            if (station.rides_started > max_start_val or
                    (station.rides_started == max_start_val and
                     station.name < max_start_name)):
                max_start_val = station.rides_started
                max_start_name = station.name
            if (station.rides_ended > max_end_val or
                    (station.rides_ended == max_end_val and
                     station.name < max_end_name)):
                max_end_val = station.rides_ended
                max_end_name = station.name
            if (station.low_availability > max_low_avail_val or
                    (station.low_availability == max_low_avail_val and
                     station.name < max_low_avail_name)):
                max_low_avail_val = station.low_availability
                max_low_avail_name = station.name
            if (station.low_unoccupied > max_low_unocc_val or
                    (station.low_unoccupied == max_low_unocc_val and
                     station.name < max_low_unocc_name)):
                max_low_unocc_val = station.low_unoccupied
                max_low_unocc_name = station.name

        return {
            'max_start': (max_start_name, max_start_val),
            'max_end': (max_end_name, max_end_val),
            'max_time_low_availability': (max_low_avail_name,
                                          max_low_avail_val),
            'max_time_low_unoccupied': (max_low_unocc_name, max_low_unocc_val)
        }

    def _update_active_rides_fast(self, time: datetime) -> None:
        """Update this simulation's list of active rides for the given time.
        REQUIRED IMPLEMENTATION NOTES:
        -   see Task 5 of the assignment handout
        """
        # Do nothing if there are no events to be processed
        if self._event_pq.is_empty():
            return

        # Deal with all of the events that have an execution time of earlier
        # than the current time, as well as multiple events that may have the
        # same execution time.
        curr_event = self._event_pq.remove()

        while curr_event.time <= time:
            new_events = curr_event.process()
            for i in range(len(new_events)):
                self._event_pq.add(new_events[i])

            # Get the new current event if more events exist
            if not self._event_pq.is_empty():
                curr_event = self._event_pq.remove()
            # Otherwise, there are no more events to process
            else:
                return

        # The latest current event will always have a start time of later than
        # the current time due to the condition of the while loop, so add the
        # event back into the queue.
        self._event_pq.add(curr_event)


def create_stations(stations_file: str) -> Dict[str, 'Station']:
    """Return the stations described in the given JSON data file.
    Each key in the returned dictionary is a station id,
    and each value is the corresponding Station object.
    Note that you need to call Station(...) to create these objects!
    Precondition: stations_file matches the format specified in the
                  assignment handout.
    This function should be called *before* _read_rides because the
    rides CSV file refers to station ids.
    """
    # Read in raw data using the json library.
    with open(stations_file, encoding="utf-8") as file:
        raw_stations = json.load(file)

    stations = {}
    for s in raw_stations['stations']:
        # Extract the relevant fields from the raw station JSON.
        # s is a dictionary with the keys 'n', 's', 'la', 'lo', 'da', and 'ba'
        # as described in the assignment handout.
        # NOTE: all of the corresponding values are strings, and so you need
        # to convert some of them to numbers explicitly using int() or float().
        id_ = s['n']
        position = (s['lo'], s['la'])
        num_bikes = s['da']
        capacity = num_bikes + s['ba']
        name = s['s']
        stations[id_] = Station(position, capacity, num_bikes, name)

    return stations


def create_rides(rides_file: str,
                 stations: Dict[str, 'Station']) -> List['Ride']:
    """Return the rides described in the given CSV file.
    Lookup the station ids contained in the rides file in <stations>
    to access the corresponding Station objects.
    Ignore any ride whose start or end station is not present in <stations>.
    Precondition: rides_file matches the format specified in the
                  assignment handout.
    """
    rides = []
    with open(rides_file) as file:
        for line in csv.reader(file):
            # line is a list of strings, following the format described
            # in the assignment handout.
            #
            # Convert between a string and a datetime object
            # using the function datetime.strptime and the DATETIME_FORMAT
            # constant we defined above. Example:
            # >>> datetime.strptime('2017-06-01 8:00', DATETIME_FORMAT)
            # datetime.datetime(2017, 6, 1, 8, 0)
            start = line[1]
            end = line[3]

            # Ignore rides that start or end at nonexistant stations
            if start in stations and end in stations:
                start_time = (datetime.strptime(line[0], DATETIME_FORMAT))
                end_time = (datetime.strptime(line[2], DATETIME_FORMAT))
                rides.append(Ride(stations[start], stations[end], (start_time,
                                                                   end_time)))

    return rides


class Event:
    """An event in the bike share simulation.
    Events are ordered by their timestamp.
    === Attributes ===
    simulation:
        A 'reference' to which Simulation the Event belongs to.
    time:
        The time corresponding to when the Event should be executed at.
    """
    simulation: 'Simulation'
    time: datetime

    def __init__(self, simulation: 'Simulation', time: datetime) -> None:
        """Initialize a new event."""
        self.simulation = simulation
        self.time = time

    def __lt__(self, other: 'Event') -> bool:
        """Return whether this event is less than <other>.
        Events are ordered by their timestamp.
        """
        return self.time < other.time

    def process(self) -> List['Event']:
        """Process this event by updating the state of the simulation.
        Return a list of new events spawned by this event.
        """
        raise NotImplementedError


class RideStartEvent(Event):
    """An event corresponding to the start of a ride.
    === Additional Attributes ===
    ride:
        A ride object corresponding to the RideStartEvent's ride. It allows
        ride-specific information to be accessible.
    """
    # Attribute types
    ride: Ride

    def __init__(self, simulation: 'Simulation', time: datetime, ride: 'Ride')\
            -> None:
        """Initialize a new ride start event."""
        Event.__init__(self, simulation, time)
        self.ride = ride

    def process(self) -> List['Event']:
        """Process this event by updating the state of the simulation.
        Return a list of new events spawned by this event.
        """
        # Run only if the station has enough bikes for a ride
        if self.ride.start.num_bikes > 0:
            self.simulation.active_rides.append(self.ride)

            # Only increase stations' ride start statistics if the ride starts
            # after the simulation's starting time.
            if self.time >= self.simulation.start_time:
                self.ride.start.rides_started += 1
                self.ride.start.num_bikes -= 1

            return [RideEndEvent(self.simulation, self.ride.end_time,
                                 self.ride)]

        # Otherwise, no new events need to be returned
        else:
            return []


class RideEndEvent(Event):
    """An event corresponding to the start of a ride.
    === Additional Attributes ===
    ride:
        A ride object corresponding to the RideEndEvent's ride. It allows
        ride-specific information to be accessible.
    """
    # Attribute types
    ride: Ride

    def __init__(self, simulation: 'Simulation', time: datetime, ride: 'Ride')\
            -> None:
        """Initialize a new ride end event."""
        Event.__init__(self, simulation, time)
        self.ride = ride

    def process(self) -> List['Event']:
        """Process this event by updating the state of the simulation.
        No events are generated by this event, so return an empty list.
        """
        self.simulation.active_rides.remove(self.ride)
        if self.ride.end.num_bikes < self.ride.end.capacity:
            self.ride.end.rides_ended += 1
            self.ride.end.num_bikes += 1
        return []


def sample_simulation() -> Dict[str, Tuple[str, float]]:
    """Run a sample simulation. For testing purposes only."""
    sim = Simulation('stations.json', 'custom_rides_1.csv')

    # Print sample station information
    # print(f"Number of stations: {len(sim.all_stations)}\n")
    # for station in sim.all_stations:
    #     print(f"Station name: {sim.all_stations[station].name}")
    #     print(f"Position: {sim.all_stations[station].location}")
    #     print(f"Capacity: {sim.all_stations[station].capacity}")
    #     print(f"Bikes: {sim.all_stations[station].num_bikes}\n")

    # Print sample ride information
    # print(f"Number of rides: {len(sim.all_rides)}")
    # for ride in sim.all_rides:
    #     print(f"Start station: {ride.start.name}")
    #     print(f"Start time: {ride.start_time}")
    #     print(f"End station: {ride.end.name}")
    #     print(f"End time: {ride.end_time}\n")

    sim.run(datetime(2017, 5, 1, 0, 0, 0), datetime(2017, 5, 1, 0, 0, 0))
    return sim.calculate_statistics()


if __name__ == '__main__':
    # Uncomment these lines when you want to check your work using python_ta!
    # import python_ta
    # python_ta.check_all(config={
    #     'allowed-io': ['create_stations', 'create_rides'],
    #     'allowed-import-modules': [
    #         'doctest', 'python_ta', 'typing',
    #         'csv', 'datetime', 'json',
    #         'bikeshare', 'container', 'visualizer'
    #     ]
    # })
    print(sample_simulation())
