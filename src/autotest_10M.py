from datetime import datetime
import os
import pygame
from simulation import Simulation


def test_auto_simulation_1():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 17, 21, 0), datetime(2017, 5, 1, 17, 57, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Métro Peel (de Maisonneuve / Stanley)', 8)
    assert stats['max_end'] == ('Métro Mont-Royal (Rivard / du Mont-Royal)', 7)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 2160)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 2160)

def test_auto_simulation_2():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 20, 32, 0), datetime(2017, 5, 1, 20, 36, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('de Gaspé / St-Viateur', 3)
    assert stats['max_end'] == ('Berri / de Maisonneuve', 1)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 240)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 240)

def test_auto_simulation_3():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 6, 2, 0), datetime(2017, 5, 1, 7, 28, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Marquette / Laurier', 3)
    assert stats['max_end'] == ('Métro Papineau (Cartier / Ste-Catherine)', 4)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 5160)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 5160)

def test_auto_simulation_4():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 4, 26, 0), datetime(2017, 5, 1, 5, 40, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('du Parc-La Fontaine / Roy', 2)
    assert stats['max_end'] == ('Berri / de Maisonneuve', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 4440)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 4440)

def test_auto_simulation_5():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 8, 1, 0), datetime(2017, 5, 1, 9, 12, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('St-André / Duluth', 6)
    assert stats['max_end'] == ('Métro Place-des-Arts (de Maisonneuve / de Bleury)', 4)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 4260)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 4260)

def test_auto_simulation_6():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 15, 21, 0), datetime(2017, 5, 1, 15, 55, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Métro Mont-Royal (Rivard / du Mont-Royal)', 4)
    assert stats['max_end'] == ('Boyer / du Mont-Royal', 3)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 2040)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 2040)

def test_auto_simulation_7():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 21, 41, 0), datetime(2017, 5, 1, 22, 24, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('du Mont-Royal / Clark', 4)
    assert stats['max_end'] == ('Beaudry / Sherbrooke', 3)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 2580)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 2580)

def test_auto_simulation_8():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 11, 1, 0), datetime(2017, 5, 1, 12, 47, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Métro Laurier (Rivard / Laurier)', 5)
    assert stats['max_end'] == ('Jeanne-Mance / St-Viateur', 5)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 6360)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 6360)

def test_auto_simulation_9():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 8, 51, 0), datetime(2017, 5, 1, 9, 29, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Métro Mont-Royal (Rivard / du Mont-Royal)', 4)
    assert stats['max_end'] == ('St-Dominique / St-Viateur', 6)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 2280)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 2280)

def test_auto_simulation_10():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 14, 34, 0), datetime(2017, 5, 1, 15, 41, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Milton / Université', 8)
    assert stats['max_end'] == ('Métro Mont-Royal (Rivard / du Mont-Royal)', 6)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 4020)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 4020)


if __name__ == '__main__':
    import pytest
    pytest.main(['autotest_10M.py'])
