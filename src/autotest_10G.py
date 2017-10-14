from datetime import datetime
import os
import pygame
from simulation import Simulation


def test_auto_simulation_1():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 6, 1, 0), datetime(2017, 5, 1, 7, 20, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Benny / de Monkland', 2)
    assert stats['max_end'] == ('Métro Papineau (Cartier / Ste-Catherine)', 4)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 4740)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 4740)

def test_auto_simulation_2():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 17, 19, 0), datetime(2017, 5, 1, 18, 50, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Métro Mont-Royal (Rivard / du Mont-Royal)', 16)
    assert stats['max_end'] == ('Métro Mont-Royal (Rivard / du Mont-Royal)', 13)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 5460)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 5460)

def test_auto_simulation_3():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 12, 28, 0), datetime(2017, 5, 1, 12, 55, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('de Maisonneuve / Robert-Bourassa', 3)
    assert stats['max_end'] == ('Jeanne-Mance / St-Viateur', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 1620)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 1620)

def test_auto_simulation_4():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 8, 20, 0), datetime(2017, 5, 1, 8, 35, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Bernard / Jeanne-Mance', 2)
    assert stats['max_end'] == ('de Bordeaux / Rachel', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 900)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 900)

def test_auto_simulation_5():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 7, 19, 0), datetime(2017, 5, 1, 8, 15, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Marquette / Laurier', 4)
    assert stats['max_end'] == ('Métro Mont-Royal (Rivard / du Mont-Royal)', 3)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 3360)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 3360)

def test_auto_simulation_6():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 3, 55, 0), datetime(2017, 5, 1, 4, 36, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Boyer / du Mont-Royal', 1)
    assert stats['max_end'] == ('Clark / St-Viateur', 1)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 2460)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 2460)

def test_auto_simulation_7():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 8, 10, 0), datetime(2017, 5, 1, 8, 34, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('St-André / Duluth', 4)
    assert stats['max_end'] == ('Métro Place-des-Arts (de Maisonneuve / de Bleury)', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 1440)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 1440)

def test_auto_simulation_8():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 15, 19, 0), datetime(2017, 5, 1, 15, 54, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Métro Mont-Royal (Rivard / du Mont-Royal)', 4)
    assert stats['max_end'] == ('Boyer / du Mont-Royal', 3)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 2100)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 2100)

def test_auto_simulation_9():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 14, 3, 0), datetime(2017, 5, 1, 15, 37, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Milton / Université', 10)
    assert stats['max_end'] == ('Métro Mont-Royal (Rivard / du Mont-Royal)', 6)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 5640)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 5640)

def test_auto_simulation_10():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 7, 5, 0), datetime(2017, 5, 1, 7, 50, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Marquette / Laurier', 3)
    assert stats['max_end'] == ('Métro Mont-Royal (Rivard / du Mont-Royal)', 3)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 2700)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 2700)


if __name__ == '__main__':
    import pytest
    pytest.main(['autotest_10G.py'])
