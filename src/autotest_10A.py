from datetime import datetime
import os
import pygame
from simulation import Simulation


def test_auto_simulation_1():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 15, 19, 0), datetime(2017, 5, 1, 15, 55, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Métro Mont-Royal (Rivard / du Mont-Royal)', 4)
    assert stats['max_end'] == ('Boyer / du Mont-Royal', 3)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 2160)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 2160)

def test_auto_simulation_2():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 11, 49, 0), datetime(2017, 5, 1, 12, 4, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Métro Place-des-Arts (de Maisonneuve / de Bleury)', 3)
    assert stats['max_end'] == ('Jeanne-Mance / St-Viateur', 3)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 900)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 900)

def test_auto_simulation_3():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 10, 5, 0), datetime(2017, 5, 1, 11, 51, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Jeanne-Mance / St-Viateur', 5)
    assert stats['max_end'] == ('des Érables / du Mont-Royal', 4)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 6360)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 6360)

def test_auto_simulation_4():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 2, 21, 0), datetime(2017, 5, 1, 2, 38, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('10e Avenue / Rosemont', 0)
    assert stats['max_end'] == ('Crescent / René-Lévesque', 1)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 1020)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 1020)

def test_auto_simulation_5():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 19, 59, 0), datetime(2017, 5, 1, 20, 27, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Métro Laurier (Rivard / Laurier)', 5)
    assert stats['max_end'] == ('Clark / St-Viateur', 3)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 1680)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 1680)

def test_auto_simulation_6():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 7, 18, 0), datetime(2017, 5, 1, 7, 39, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Alexandre-DeSève / de Maisonneuve', 2)
    assert stats['max_end'] == ('Métro Laurier (Rivard / Laurier)', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 1260)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 1260)

def test_auto_simulation_7():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 21, 18, 0), datetime(2017, 5, 1, 22, 8, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Mackay /de Maisonneuve (Sud)', 4)
    assert stats['max_end'] == ('Boyer / du Mont-Royal', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 3000)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 3000)

def test_auto_simulation_8():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 10, 5, 0), datetime(2017, 5, 1, 11, 30, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Clark / Prince-Arthur', 3)
    assert stats['max_end'] == ('Métro Laurier (Rivard / Laurier)', 3)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 5100)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 5100)

def test_auto_simulation_9():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 16, 28, 0), datetime(2017, 5, 1, 16, 35, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('McGill / Place d\'Youville', 2)
    assert stats['max_end'] == ('Métro Laurier (Rivard / Laurier)', 3)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 420)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 420)

def test_auto_simulation_10():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 11, 51, 0), datetime(2017, 5, 1, 12, 34, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('St-André / Ste-Catherine', 3)
    assert stats['max_end'] == ('4e avenue / Masson', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 2580)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 2580)


if __name__ == '__main__':
    import pytest
    pytest.main(['autotest_10A.py'])
