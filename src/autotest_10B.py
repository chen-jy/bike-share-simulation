from datetime import datetime
import os
import pygame
from simulation import Simulation


def test_auto_simulation_1():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 4, 0, 0), datetime(2017, 5, 1, 5, 50, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('du Parc-La Fontaine / Roy', 2)
    assert stats['max_end'] == ('Berri / de Maisonneuve', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 6600)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 6600)

def test_auto_simulation_2():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 10, 7, 0), datetime(2017, 5, 1, 10, 52, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Métro Mont-Royal (Rivard / du Mont-Royal)', 3)
    assert stats['max_end'] == ('de la Commune / St-Sulpice', 3)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 2700)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 2700)

def test_auto_simulation_3():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 2, 55, 0), datetime(2017, 5, 1, 2, 56, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('10e Avenue / Rosemont', 0)
    assert stats['max_end'] == ('10e Avenue / Rosemont', 0)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 60)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 60)

def test_auto_simulation_4():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 15, 21, 0), datetime(2017, 5, 1, 16, 33, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Métro Mont-Royal (Rivard / du Mont-Royal)', 8)
    assert stats['max_end'] == ('Gilford / Brébeuf', 5)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 4320)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 4320)

def test_auto_simulation_5():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 2, 59, 0), datetime(2017, 5, 1, 3, 6, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('St-Cuthbert / St-Urbain', 1)
    assert stats['max_end'] == ('10e Avenue / Rosemont', 0)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 420)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 420)

def test_auto_simulation_6():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 12, 1, 0), datetime(2017, 5, 1, 12, 20, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Métro Peel (de Maisonneuve / Stanley)', 2)
    assert stats['max_end'] == ('15e avenue / Masson', 1)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 1140)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 1140)

def test_auto_simulation_7():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 12, 42, 0), datetime(2017, 5, 1, 12, 51, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('7e avenue / St-Joseph', 1)
    assert stats['max_end'] == ('16e avenue / Beaubien', 1)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 540)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 540)

def test_auto_simulation_8():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 21, 4, 0), datetime(2017, 5, 1, 22, 31, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Mackay /de Maisonneuve (Sud)', 6)
    assert stats['max_end'] == ('Prince-Arthur / du Parc', 4)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 5220)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 5220)

def test_auto_simulation_9():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 15, 3, 0), datetime(2017, 5, 1, 15, 28, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Marquette / du Mont-Royal', 3)
    assert stats['max_end'] == ('Ste-Famille / Sherbrooke', 3)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 1500)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 1500)

def test_auto_simulation_10():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 13, 27, 0), datetime(2017, 5, 1, 14, 15, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Mackay /de Maisonneuve (Sud)', 3)
    assert stats['max_end'] == ('Messier / du Mont-Royal', 3)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 2880)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 2880)


if __name__ == '__main__':
    import pytest
    pytest.main(['autotest_10B.py'])
