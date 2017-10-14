from datetime import datetime
import os
import pygame
from simulation import Simulation


def test_auto_simulation_1():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 9, 29, 0), datetime(2017, 5, 1, 9, 57, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Bordeaux / Masson', 2)
    assert stats['max_end'] == ('Métro St-Laurent (de Maisonneuve / St-Laurent)', 4)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 1680)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 1680)

def test_auto_simulation_2():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 19, 49, 0), datetime(2017, 5, 1, 19, 57, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Métro Laurier (Rivard / Laurier)', 3)
    assert stats['max_end'] == ('Champlain / Ontario', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 480)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 480)

def test_auto_simulation_3():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 18, 39, 0), datetime(2017, 5, 1, 18, 56, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Duluth / St-Laurent', 3)
    assert stats['max_end'] == ('Roy / St-Laurent', 4)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 1020)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 1020)

def test_auto_simulation_4():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 16, 52, 0), datetime(2017, 5, 1, 17, 37, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Milton / Université', 10)
    assert stats['max_end'] == ('Roy / St-Laurent', 5)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 2700)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 2700)

def test_auto_simulation_5():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 3, 35, 0), datetime(2017, 5, 1, 3, 59, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Boyer / du Mont-Royal', 2)
    assert stats['max_end'] == ('Alma / Beaubien', 1)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 1440)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 1440)

def test_auto_simulation_6():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 6, 44, 0), datetime(2017, 5, 1, 7, 26, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Clark / St-Viateur', 2)
    assert stats['max_end'] == ('Clark / Laurier', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 2520)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 2520)

def test_auto_simulation_7():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 16, 23, 0), datetime(2017, 5, 1, 17, 32, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Milton / Université', 11)
    assert stats['max_end'] == ('Métro Peel (de Maisonneuve / Stanley)', 6)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 4140)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 4140)

def test_auto_simulation_8():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 4, 22, 0), datetime(2017, 5, 1, 5, 12, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Mackay /de Maisonneuve (Sud)', 1)
    assert stats['max_end'] == ('Berri / de Maisonneuve', 1)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 3000)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 3000)

def test_auto_simulation_9():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 14, 14, 0), datetime(2017, 5, 1, 14, 36, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('de la Commune / St-Sulpice', 3)
    assert stats['max_end'] == ('Basin / Richmond', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 1320)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 1320)

def test_auto_simulation_10():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 6, 6, 0), datetime(2017, 5, 1, 6, 10, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Laval / du Mont-Royal', 1)
    assert stats['max_end'] == ('Place Jean-Paul Riopelle (Viger / de Bleury)', 1)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 240)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 240)


if __name__ == '__main__':
    import pytest
    pytest.main(['autotest_10J.py'])
