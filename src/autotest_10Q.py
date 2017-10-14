from datetime import datetime
import os
import pygame
from simulation import Simulation


def test_auto_simulation_1():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 19, 40, 0), datetime(2017, 5, 1, 19, 56, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Métro Laurier (Rivard / Laurier)', 3)
    assert stats['max_end'] == ('Chabot / du Mont-Royal', 3)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 960)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 960)

def test_auto_simulation_2():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 11, 25, 0), datetime(2017, 5, 1, 12, 36, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Métro Place-des-Arts (de Maisonneuve / de Bleury)', 5)
    assert stats['max_end'] == ('Jeanne-Mance / St-Viateur', 4)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 4260)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 4260)

def test_auto_simulation_3():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 5, 24, 0), datetime(2017, 5, 1, 6, 29, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('5e avenue / de Verdun', 1)
    assert stats['max_end'] == ('Ste-Catherine / St-Denis', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 3900)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 3900)

def test_auto_simulation_4():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 11, 20, 0), datetime(2017, 5, 1, 11, 48, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Jeanne-Mance / St-Viateur', 3)
    assert stats['max_end'] == ('Métro Peel (de Maisonneuve / Stanley)', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 1680)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 1680)

def test_auto_simulation_5():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 4, 30, 0), datetime(2017, 5, 1, 5, 19, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Mackay /de Maisonneuve (Sud)', 1)
    assert stats['max_end'] == ('Berri / de Maisonneuve', 1)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 2940)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 2940)

def test_auto_simulation_6():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 7, 46, 0), datetime(2017, 5, 1, 8, 30, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('St-André / Duluth', 4)
    assert stats['max_end'] == ('Métro Place-des-Arts (de Maisonneuve / de Bleury)', 4)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 2640)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 2640)

def test_auto_simulation_7():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 8, 18, 0), datetime(2017, 5, 1, 9, 50, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Notre-Dame / Peel', 5)
    assert stats['max_end'] == ('Notre-Dame / Peel', 8)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 5520)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 5520)

def test_auto_simulation_8():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 20, 57, 0), datetime(2017, 5, 1, 20, 57, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('10e Avenue / Rosemont', 0)
    assert stats['max_end'] == ('10e Avenue / Rosemont', 0)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 60)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 60)

def test_auto_simulation_9():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 10, 37, 0), datetime(2017, 5, 1, 11, 41, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Clark / Prince-Arthur', 3)
    assert stats['max_end'] == ('Métro Laurier (Rivard / Laurier)', 3)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 3840)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 3840)

def test_auto_simulation_10():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 5, 14, 0), datetime(2017, 5, 1, 6, 7, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('5e avenue / de Verdun', 1)
    assert stats['max_end'] == ('de Maisonneuve / Robert-Bourassa', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 3180)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 3180)


if __name__ == '__main__':
    import pytest
    pytest.main(['autotest_10Q.py'])
