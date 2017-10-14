from datetime import datetime
import os
import pygame
from simulation import Simulation


def test_auto_simulation_1():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 13, 32, 0), datetime(2017, 5, 1, 14, 43, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Milton / Université', 6)
    assert stats['max_end'] == ('Métro Mont-Royal (Rivard / du Mont-Royal)', 4)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 4260)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 4260)

def test_auto_simulation_2():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 4, 39, 0), datetime(2017, 5, 1, 5, 52, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('du Parc-La Fontaine / Roy', 2)
    assert stats['max_end'] == ('Berri / de Maisonneuve', 1)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 4380)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 4380)

def test_auto_simulation_3():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 14, 14, 0), datetime(2017, 5, 1, 15, 21, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Milton / Université', 8)
    assert stats['max_end'] == ('Métro Mont-Royal (Rivard / du Mont-Royal)', 5)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 4020)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 4020)

def test_auto_simulation_4():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 10, 53, 0), datetime(2017, 5, 1, 10, 56, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Métro Bonaventure (de la Gauchetière / Mansfield)', 2)
    assert stats['max_end'] == ('Ste-Famille / Sherbrooke', 1)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 180)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 180)

def test_auto_simulation_5():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 17, 49, 0), datetime(2017, 5, 1, 18, 13, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Métro Mont-Royal (Rivard / du Mont-Royal)', 6)
    assert stats['max_end'] == ('St-André / Duluth', 7)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 1440)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 1440)

def test_auto_simulation_6():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 16, 54, 0), datetime(2017, 5, 1, 17, 32, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Milton / Université', 9)
    assert stats['max_end'] == ('Ann / William', 4)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 2280)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 2280)

def test_auto_simulation_7():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 2, 16, 0), datetime(2017, 5, 1, 2, 24, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('St-Mathieu /Ste-Catherine', 1)
    assert stats['max_end'] == ('10e Avenue / Rosemont', 0)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 480)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 480)

def test_auto_simulation_8():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 21, 10, 0), datetime(2017, 5, 1, 22, 12, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Duluth / St-Laurent', 4)
    assert stats['max_end'] == ('Beaudry / Sherbrooke', 3)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 3720)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 3720)

def test_auto_simulation_9():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 15, 2, 0), datetime(2017, 5, 1, 16, 51, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Milton / Université', 9)
    assert stats['max_end'] == ('Marquette / du Mont-Royal', 8)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 6540)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 6540)

def test_auto_simulation_10():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 19, 39, 0), datetime(2017, 5, 1, 19, 58, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Métro Laurier (Rivard / Laurier)', 3)
    assert stats['max_end'] == ('Chabot / du Mont-Royal', 3)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 1140)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 1140)


if __name__ == '__main__':
    import pytest
    pytest.main(['autotest_10F.py'])
