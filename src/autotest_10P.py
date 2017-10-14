from datetime import datetime
import os
import pygame
from simulation import Simulation


def test_auto_simulation_1():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 6, 45, 0), datetime(2017, 5, 1, 6, 52, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Berri / St-Grégoire', 1)
    assert stats['max_end'] == ('Berri / de Maisonneuve', 1)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 420)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 420)

def test_auto_simulation_2():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 12, 9, 0), datetime(2017, 5, 1, 12, 33, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Gilford / Brébeuf', 2)
    assert stats['max_end'] == ('Napoléon /  St-Dominique', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 1440)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 1440)

def test_auto_simulation_3():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 9, 2, 0), datetime(2017, 5, 1, 9, 28, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Métro Mont-Royal (Rivard / du Mont-Royal)', 3)
    assert stats['max_end'] == ('St-Dominique / St-Viateur', 3)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 1560)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 1560)

def test_auto_simulation_4():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 3, 30, 0), datetime(2017, 5, 1, 3, 46, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Boyer / du Mont-Royal', 1)
    assert stats['max_end'] == ('Atwater / Sherbrooke', 1)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 960)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 960)

def test_auto_simulation_5():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 0, 52, 0), datetime(2017, 5, 1, 1, 54, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Berri / St-Grégoire', 2)
    assert stats['max_end'] == ('Prince-Arthur / Ste-Famille', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 3720)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 3720)

def test_auto_simulation_6():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 20, 33, 0), datetime(2017, 5, 1, 20, 42, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Aylwin / Ontario', 2)
    assert stats['max_end'] == ('Mackay /de Maisonneuve (Sud)', 3)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 540)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 540)

def test_auto_simulation_7():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 21, 57, 0), datetime(2017, 5, 1, 21, 57, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('10e Avenue / Rosemont', 0)
    assert stats['max_end'] == ('10e Avenue / Rosemont', 0)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 60)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 60)

def test_auto_simulation_8():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 6, 18, 0), datetime(2017, 5, 1, 6, 55, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Benny / de Monkland', 2)
    assert stats['max_end'] == ('Métro Mont-Royal (Rivard / du Mont-Royal)', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 2220)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 2220)

def test_auto_simulation_9():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 3, 41, 0), datetime(2017, 5, 1, 3, 54, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Boyer / du Mont-Royal', 1)
    assert stats['max_end'] == ('Alma / Beaubien', 1)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 780)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 780)

def test_auto_simulation_10():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 20, 8, 0), datetime(2017, 5, 1, 20, 34, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('du Mont-Royal / Clark', 4)
    assert stats['max_end'] == ('du Mont-Royal / Clark', 4)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 1560)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 1560)


if __name__ == '__main__':
    import pytest
    pytest.main(['autotest_10P.py'])
