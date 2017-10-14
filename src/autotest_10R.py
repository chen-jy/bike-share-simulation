from datetime import datetime
import os
import pygame
from simulation import Simulation


def test_auto_simulation_1():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 14, 40, 0), datetime(2017, 5, 1, 15, 42, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Milton / Université', 7)
    assert stats['max_end'] == ('Métro Mont-Royal (Rivard / du Mont-Royal)', 6)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 3720)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 3720)

def test_auto_simulation_2():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 10, 47, 0), datetime(2017, 5, 1, 10, 50, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Chomedey / de Maisonneuve', 1)
    assert stats['max_end'] == ('Drummond / de Maisonneuve', 1)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 180)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 180)

def test_auto_simulation_3():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 19, 12, 0), datetime(2017, 5, 1, 19, 47, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Métro Laurier (Rivard / Laurier)', 7)
    assert stats['max_end'] == ('Marquette / Laurier', 4)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 2100)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 2100)

def test_auto_simulation_4():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 4, 17, 0), datetime(2017, 5, 1, 4, 26, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Boyer / du Mont-Royal', 1)
    assert stats['max_end'] == ('Clark / St-Viateur', 1)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 540)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 540)

def test_auto_simulation_5():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 9, 22, 0), datetime(2017, 5, 1, 9, 50, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Notre-Dame / Peel', 3)
    assert stats['max_end'] == ('Notre-Dame / Peel', 3)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 1680)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 1680)

def test_auto_simulation_6():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 19, 35, 0), datetime(2017, 5, 1, 19, 47, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Chomedey / de Maisonneuve', 2)
    assert stats['max_end'] == ('Hampton / de Monkland', 3)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 720)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 720)

def test_auto_simulation_7():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 17, 34, 0), datetime(2017, 5, 1, 17, 48, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('de Maisonneuve / Mansfield', 5)
    assert stats['max_end'] == ('Fullum / Sherbrooke ', 3)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 840)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 840)

def test_auto_simulation_8():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 2, 35, 0), datetime(2017, 5, 1, 2, 45, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('de la Commune / Place Jacques-Cartier', 1)
    assert stats['max_end'] == ('de la Commune / St-Sulpice', 1)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 600)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 600)

def test_auto_simulation_9():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 6, 20, 0), datetime(2017, 5, 1, 7, 0, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Benny / de Monkland', 2)
    assert stats['max_end'] == ('Métro Mont-Royal (Rivard / du Mont-Royal)', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 2400)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 2400)

def test_auto_simulation_10():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 5, 26, 0), datetime(2017, 5, 1, 6, 21, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('5e avenue / de Verdun', 1)
    assert stats['max_end'] == ('Ste-Catherine / St-Denis', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 3300)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 3300)


if __name__ == '__main__':
    import pytest
    pytest.main(['autotest_10R.py'])
