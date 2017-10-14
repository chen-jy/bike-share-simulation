from datetime import datetime
import os
import pygame
from simulation import Simulation


def test_auto_simulation_1():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 19, 36, 0), datetime(2017, 5, 1, 19, 53, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Métro Laurier (Rivard / Laurier)', 3)
    assert stats['max_end'] == ('Chabot / du Mont-Royal', 3)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 1020)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 1020)

def test_auto_simulation_2():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 18, 0, 0), datetime(2017, 5, 1, 19, 23, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Métro Mont-Royal (Rivard / du Mont-Royal)', 14)
    assert stats['max_end'] == ('Métro Laurier (Rivard / Laurier)', 9)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 4980)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 4980)

def test_auto_simulation_3():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 0, 11, 0), datetime(2017, 5, 1, 0, 16, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Berri / Sherbrooke', 1)
    assert stats['max_end'] == ('Alexandre-DeSève / de Maisonneuve', 1)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 300)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 300)

def test_auto_simulation_4():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 14, 9, 0), datetime(2017, 5, 1, 14, 24, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('de la Commune / St-Sulpice', 3)
    assert stats['max_end'] == ('de la Montagne / Sherbrooke', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 900)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 900)

def test_auto_simulation_5():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 1, 58, 0), datetime(2017, 5, 1, 2, 22, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Marie-Anne / de la Roche', 1)
    assert stats['max_end'] == ('Champagneur / Jean-Talon', 1)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 1440)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 1440)

def test_auto_simulation_6():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 2, 43, 0), datetime(2017, 5, 1, 2, 45, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('10e Avenue / Rosemont', 0)
    assert stats['max_end'] == ('de la Commune / St-Sulpice', 1)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 120)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 120)

def test_auto_simulation_7():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 13, 42, 0), datetime(2017, 5, 1, 13, 46, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Chabot / de Bellechasse', 1)
    assert stats['max_end'] == ('de la Commune / Berri', 3)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 240)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 240)

def test_auto_simulation_8():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 6, 1, 0), datetime(2017, 5, 1, 6, 1, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Park Row O / Sherbrooke', 1)
    assert stats['max_end'] == ('10e Avenue / Rosemont', 0)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 60)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 60)

def test_auto_simulation_9():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 1, 49, 0), datetime(2017, 5, 1, 1, 50, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('10e Avenue / Rosemont', 0)
    assert stats['max_end'] == ('Rachel / Brébeuf', 1)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 60)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 60)

def test_auto_simulation_10():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 9, 57, 0), datetime(2017, 5, 1, 10, 5, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('de la Commune / Place Jacques-Cartier', 2)
    assert stats['max_end'] == ('Cartier / Marie-Anne', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 480)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 480)


if __name__ == '__main__':
    import pytest
    pytest.main(['autotest_10D.py'])
