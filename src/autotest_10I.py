from datetime import datetime
import os
import pygame
from simulation import Simulation


def test_auto_simulation_1():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 1, 27, 0), datetime(2017, 5, 1, 1, 52, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Berri / St-Grégoire', 2)
    assert stats['max_end'] == ('du Mont-Royal / Clark', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 1500)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 1500)

def test_auto_simulation_2():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 4, 39, 0), datetime(2017, 5, 1, 5, 57, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('du Parc-La Fontaine / Roy', 2)
    assert stats['max_end'] == ('de Maisonneuve / Robert-Bourassa', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 4680)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 4680)

def test_auto_simulation_3():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 7, 38, 0), datetime(2017, 5, 1, 7, 51, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Gilford / Brébeuf', 2)
    assert stats['max_end'] == ('De la Commune / King', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 780)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 780)

def test_auto_simulation_4():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 20, 28, 0), datetime(2017, 5, 1, 20, 58, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Marquette / du Mont-Royal', 4)
    assert stats['max_end'] == ('Ann / William', 4)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 1800)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 1800)

def test_auto_simulation_5():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 19, 1, 0), datetime(2017, 5, 1, 19, 10, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Drummond / de Maisonneuve', 2)
    assert stats['max_end'] == ('Gary-Carter / St-Laurent', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 540)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 540)

def test_auto_simulation_6():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 19, 15, 0), datetime(2017, 5, 1, 20, 21, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Métro Laurier (Rivard / Laurier)', 14)
    assert stats['max_end'] == ('Marquette / Laurier', 7)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 3960)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 3960)

def test_auto_simulation_7():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 17, 35, 0), datetime(2017, 5, 1, 18, 30, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Métro Mont-Royal (Rivard / du Mont-Royal)', 9)
    assert stats['max_end'] == ('Notre-Dame / Peel', 8)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 3300)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 3300)

def test_auto_simulation_8():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 20, 28, 0), datetime(2017, 5, 1, 20, 40, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Mackay /de Maisonneuve (Sud)', 3)
    assert stats['max_end'] == ('Mackay /de Maisonneuve (Sud)', 4)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 720)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 720)

def test_auto_simulation_9():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 17, 50, 0), datetime(2017, 5, 1, 17, 54, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Drummond / de Maisonneuve', 2)
    assert stats['max_end'] == ('Benny / de Monkland', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 240)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 240)

def test_auto_simulation_10():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 8, 37, 0), datetime(2017, 5, 1, 9, 34, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Métro Mont-Royal (Rivard / du Mont-Royal)', 4)
    assert stats['max_end'] == ('St-Dominique / St-Viateur', 7)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 3420)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 3420)


if __name__ == '__main__':
    import pytest
    pytest.main(['autotest_10I.py'])
