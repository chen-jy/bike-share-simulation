from datetime import datetime
import os
import pygame
from simulation import Simulation


def test_auto_simulation_1():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 13, 59, 0), datetime(2017, 5, 1, 13, 59, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('10e Avenue / Rosemont', 0)
    assert stats['max_end'] == ('10e Avenue / Rosemont', 0)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 60)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 60)

def test_auto_simulation_2():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 12, 16, 0), datetime(2017, 5, 1, 12, 56, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('de Maisonneuve / Robert-Bourassa', 3)
    assert stats['max_end'] == ('Wolfe / René-Lévesque', 3)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 2400)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 2400)

def test_auto_simulation_3():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 13, 35, 0), datetime(2017, 5, 1, 13, 48, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Milton / Clark', 2)
    assert stats['max_end'] == ('de la Commune / Berri', 3)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 780)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 780)

def test_auto_simulation_4():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 5, 3, 0), datetime(2017, 5, 1, 5, 3, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('10e Avenue / Rosemont', 0)
    assert stats['max_end'] == ('10e Avenue / Rosemont', 0)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 60)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 60)

def test_auto_simulation_5():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 13, 32, 0), datetime(2017, 5, 1, 13, 40, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('1ère avenue / Rosemont', 1)
    assert stats['max_end'] == ('Alexandre-DeSève / de Maisonneuve', 1)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 480)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 480)

def test_auto_simulation_6():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 16, 52, 0), datetime(2017, 5, 1, 16, 58, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Mansfield / René-Lévesque', 2)
    assert stats['max_end'] == ('des Seigneurs / Workman', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 360)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 360)

def test_auto_simulation_7():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 20, 0, 0), datetime(2017, 5, 1, 20, 15, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Métro Laurier (Rivard / Laurier)', 4)
    assert stats['max_end'] == ('1ère avenue / Masson', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 900)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 900)

def test_auto_simulation_8():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 12, 46, 0), datetime(2017, 5, 1, 12, 50, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Cartier / St-Joseph', 1)
    assert stats['max_end'] == ('Bernard / Clark', 1)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 240)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 240)

def test_auto_simulation_9():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 8, 31, 0), datetime(2017, 5, 1, 9, 50, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('du Mont-Royal / Clark', 5)
    assert stats['max_end'] == ('Notre-Dame / Peel', 8)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 4740)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 4740)

def test_auto_simulation_10():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 4, 34, 0), datetime(2017, 5, 1, 4, 39, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('10e Avenue / Rosemont', 0)
    assert stats['max_end'] == ('Berri / de Maisonneuve', 1)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 300)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 300)


if __name__ == '__main__':
    import pytest
    pytest.main(['autotest_10H.py'])
