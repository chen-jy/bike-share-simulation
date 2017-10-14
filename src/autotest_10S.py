from datetime import datetime
import os
import pygame
from simulation import Simulation


def test_auto_simulation_1():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 8, 7, 0), datetime(2017, 5, 1, 9, 16, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('St-André / Duluth', 7)
    assert stats['max_end'] == ('Notre-Dame / Peel', 4)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 4140)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 4140)

def test_auto_simulation_2():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 17, 45, 0), datetime(2017, 5, 1, 17, 47, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Gatineau/Swail', 2)
    assert stats['max_end'] == ('3e avenue / Dandurand', 1)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 120)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 120)

def test_auto_simulation_3():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 8, 8, 0), datetime(2017, 5, 1, 8, 32, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('St-André / Duluth', 4)
    assert stats['max_end'] == ('Marmier / St-Denis', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 1440)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 1440)

def test_auto_simulation_4():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 6, 37, 0), datetime(2017, 5, 1, 6, 59, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Clark / St-Viateur', 2)
    assert stats['max_end'] == ('Métro Mont-Royal (Rivard / du Mont-Royal)', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 1320)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 1320)

def test_auto_simulation_5():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 6, 21, 0), datetime(2017, 5, 1, 6, 43, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Benny / de Monkland', 2)
    assert stats['max_end'] == ('Métro Mont-Royal (Rivard / du Mont-Royal)', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 1320)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 1320)

def test_auto_simulation_6():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 10, 36, 0), datetime(2017, 5, 1, 11, 33, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Clark / Prince-Arthur', 3)
    assert stats['max_end'] == ('Métro Laurier (Rivard / Laurier)', 3)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 3420)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 3420)

def test_auto_simulation_7():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 7, 17, 0), datetime(2017, 5, 1, 8, 30, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Marquette / Laurier', 4)
    assert stats['max_end'] == ('Métro Mont-Royal (Rivard / du Mont-Royal)', 4)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 4380)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 4380)

def test_auto_simulation_8():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 5, 43, 0), datetime(2017, 5, 1, 5, 48, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('5e avenue / de Verdun', 1)
    assert stats['max_end'] == ('Pierre-de-Coubertin / Aird', 1)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 300)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 300)

def test_auto_simulation_9():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 9, 57, 0), datetime(2017, 5, 1, 10, 31, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('1ère avenue / Rosemont', 2)
    assert stats['max_end'] == ('Cartier / Marie-Anne', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 2040)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 2040)

def test_auto_simulation_10():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 1, 18, 0), datetime(2017, 5, 1, 2, 19, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Berri / St-Grégoire', 2)
    assert stats['max_end'] == ('du Mont-Royal / Clark', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 3660)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 3660)


if __name__ == '__main__':
    import pytest
    pytest.main(['autotest_10S.py'])
