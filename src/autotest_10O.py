from datetime import datetime
import os
import pygame
from simulation import Simulation


def test_auto_simulation_1():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 1, 56, 0), datetime(2017, 5, 1, 2, 16, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Marie-Anne / de la Roche', 1)
    assert stats['max_end'] == ('Champagneur / Jean-Talon', 1)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 1200)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 1200)

def test_auto_simulation_2():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 19, 44, 0), datetime(2017, 5, 1, 19, 50, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Chomedey / de Maisonneuve', 2)
    assert stats['max_end'] == ('Chabot / du Mont-Royal', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 360)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 360)

def test_auto_simulation_3():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 2, 25, 0), datetime(2017, 5, 1, 3, 39, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Boyer / Bélanger', 1)
    assert stats['max_end'] == ('Atwater / Sherbrooke', 1)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 4440)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 4440)

def test_auto_simulation_4():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 10, 18, 0), datetime(2017, 5, 1, 11, 25, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Clark / Rachel', 3)
    assert stats['max_end'] == ('Métro Laurier (Rivard / Laurier)', 3)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 4020)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 4020)

def test_auto_simulation_5():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 12, 47, 0), datetime(2017, 5, 1, 13, 52, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Milton / Université', 5)
    assert stats['max_end'] == ('Bishop / Ste-Catherine', 3)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 3900)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 3900)

def test_auto_simulation_6():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 18, 28, 0), datetime(2017, 5, 1, 18, 55, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('de l\'Esplanade / Laurier', 6)
    assert stats['max_end'] == ('Métro Laurier (Rivard / Laurier)', 4)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 1620)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 1620)

def test_auto_simulation_7():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 11, 9, 0), datetime(2017, 5, 1, 11, 38, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('9e avenue / Dandurand', 2)
    assert stats['max_end'] == ('de Maisonneuve / Robert-Bourassa', 3)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 1740)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 1740)

def test_auto_simulation_8():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 9, 2, 0), datetime(2017, 5, 1, 9, 40, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Métro Mont-Royal (Rivard / du Mont-Royal)', 3)
    assert stats['max_end'] == ('Notre-Dame / Peel', 5)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 2280)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 2280)

def test_auto_simulation_9():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 19, 40, 0), datetime(2017, 5, 1, 20, 22, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Métro Laurier (Rivard / Laurier)', 7)
    assert stats['max_end'] == ('Marquette / Laurier', 4)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 2520)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 2520)

def test_auto_simulation_10():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 2, 3, 0), datetime(2017, 5, 1, 2, 46, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Marie-Anne / de la Roche', 1)
    assert stats['max_end'] == ('Champagneur / Jean-Talon', 1)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 2580)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 2580)


if __name__ == '__main__':
    import pytest
    pytest.main(['autotest_10O.py'])
