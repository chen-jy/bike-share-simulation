from datetime import datetime
import os
import pygame
from simulation import Simulation


def test_auto_simulation_1():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 7, 42, 0), datetime(2017, 5, 1, 7, 44, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('9e avenue / Dandurand', 1)
    assert stats['max_end'] == ('De la Commune / King', 1)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 120)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 120)

def test_auto_simulation_2():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 14, 28, 0), datetime(2017, 5, 1, 15, 34, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Milton / Université', 7)
    assert stats['max_end'] == ('Métro Mont-Royal (Rivard / du Mont-Royal)', 5)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 3960)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 3960)

def test_auto_simulation_3():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 16, 37, 0), datetime(2017, 5, 1, 17, 58, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Milton / Université', 13)
    assert stats['max_end'] == ('Métro Mont-Royal (Rivard / du Mont-Royal)', 8)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 4860)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 4860)

def test_auto_simulation_4():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 7, 37, 0), datetime(2017, 5, 1, 8, 4, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Chomedey / de Maisonneuve', 2)
    assert stats['max_end'] == ('De la Commune / King', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 1620)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 1620)

def test_auto_simulation_5():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 1, 45, 0), datetime(2017, 5, 1, 2, 44, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Marie-Anne / de la Roche', 1)
    assert stats['max_end'] == ('Champagneur / Jean-Talon', 1)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 3540)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 3540)

def test_auto_simulation_6():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 5, 45, 0), datetime(2017, 5, 1, 6, 54, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Benny / de Monkland', 2)
    assert stats['max_end'] == ('Métro Mont-Royal (Rivard / du Mont-Royal)', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 4140)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 4140)

def test_auto_simulation_7():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 12, 16, 0), datetime(2017, 5, 1, 12, 23, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('de la Montagne / Sherbrooke', 2)
    assert stats['max_end'] == ('Bourbonnière / du Mont-Royal', 1)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 420)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 420)

def test_auto_simulation_8():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 12, 35, 0), datetime(2017, 5, 1, 13, 6, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('de Maisonneuve / Robert-Bourassa', 3)
    assert stats['max_end'] == ('Bishop / Ste-Catherine', 3)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 1860)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 1860)

def test_auto_simulation_9():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 19, 9, 0), datetime(2017, 5, 1, 20, 27, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Métro Laurier (Rivard / Laurier)', 16)
    assert stats['max_end'] == ('Marquette / Laurier', 8)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 4680)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 4680)

def test_auto_simulation_10():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 18, 34, 0), datetime(2017, 5, 1, 18, 48, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Métro Mont-Royal (Rivard / du Mont-Royal)', 4)
    assert stats['max_end'] == ('Sanguinet / Ontario', 3)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 840)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 840)


if __name__ == '__main__':
    import pytest
    pytest.main(['autotest_10C.py'])
