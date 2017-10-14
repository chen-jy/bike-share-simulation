from datetime import datetime
import os
import pygame
from simulation import Simulation


def test_auto_simulation_1():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 19, 33, 0), datetime(2017, 5, 1, 19, 46, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Chomedey / de Maisonneuve', 2)
    assert stats['max_end'] == ('Hampton / de Monkland', 3)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 780)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 780)

def test_auto_simulation_2():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 18, 3, 0), datetime(2017, 5, 1, 19, 2, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Métro Mont-Royal (Rivard / du Mont-Royal)', 8)
    assert stats['max_end'] == ('Métro Laurier (Rivard / Laurier)', 8)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 3540)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 3540)

def test_auto_simulation_3():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 11, 29, 0), datetime(2017, 5, 1, 12, 26, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Jeanne-Mance / St-Viateur', 4)
    assert stats['max_end'] == ('Jeanne-Mance / St-Viateur', 4)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 3420)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 3420)

def test_auto_simulation_4():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 3, 52, 0), datetime(2017, 5, 1, 4, 34, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Boyer / du Mont-Royal', 1)
    assert stats['max_end'] == ('Clark / St-Viateur', 1)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 2520)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 2520)

def test_auto_simulation_5():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 12, 45, 0), datetime(2017, 5, 1, 12, 59, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Larivière / de Lorimier', 2)
    assert stats['max_end'] == ('Bishop / Ste-Catherine', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 840)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 840)

def test_auto_simulation_6():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 12, 36, 0), datetime(2017, 5, 1, 12, 43, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('7e avenue / St-Joseph', 1)
    assert stats['max_end'] == ('Drolet / Laurier', 1)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 420)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 420)

def test_auto_simulation_7():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 16, 32, 0), datetime(2017, 5, 1, 16, 51, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Boyer / Jean-Talon', 3)
    assert stats['max_end'] == ('Marquette / du Mont-Royal', 3)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 1140)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 1140)

def test_auto_simulation_8():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 3, 29, 0), datetime(2017, 5, 1, 4, 53, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Boyer / du Mont-Royal', 3)
    assert stats['max_end'] == ('Clark / St-Viateur', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 5040)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 5040)

def test_auto_simulation_9():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 16, 33, 0), datetime(2017, 5, 1, 16, 52, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Boyer / Jean-Talon', 3)
    assert stats['max_end'] == ('Marquette / du Mont-Royal', 3)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 1140)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 1140)

def test_auto_simulation_10():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 11, 46, 0), datetime(2017, 5, 1, 11, 54, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Jeanne-Mance / St-Viateur', 2)
    assert stats['max_end'] == ('Jeanne-Mance / St-Viateur', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 480)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 480)


if __name__ == '__main__':
    import pytest
    pytest.main(['autotest_10L.py'])
