from datetime import datetime
import os
import pygame
from simulation import Simulation


def test_auto_simulation_1():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 4, 37, 0), datetime(2017, 5, 1, 5, 7, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Mackay /de Maisonneuve (Sud)', 1)
    assert stats['max_end'] == ('Berri / de Maisonneuve', 1)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 1800)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 1800)

def test_auto_simulation_2():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 15, 24, 0), datetime(2017, 5, 1, 15, 57, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Métro Mont-Royal (Rivard / du Mont-Royal)', 5)
    assert stats['max_end'] == ('Marquette / du Mont-Royal', 4)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 1980)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 1980)

def test_auto_simulation_3():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 21, 23, 0), datetime(2017, 5, 1, 22, 27, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Mackay /de Maisonneuve (Sud)', 6)
    assert stats['max_end'] == ('Beaudry / Sherbrooke', 3)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 3840)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 3840)

def test_auto_simulation_4():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 8, 16, 0), datetime(2017, 5, 1, 8, 17, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Briand / Carron', 1)
    assert stats['max_end'] == ('Métro Place-des-Arts (de Maisonneuve / de Bleury)', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 60)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 60)

def test_auto_simulation_5():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 3, 6, 0), datetime(2017, 5, 1, 4, 23, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Boyer / du Mont-Royal', 3)
    assert stats['max_end'] == ('Clark / St-Viateur', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 4620)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 4620)

def test_auto_simulation_6():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 0, 56, 0), datetime(2017, 5, 1, 1, 18, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Clark / Guilbault', 2)
    assert stats['max_end'] == ('Prince-Arthur / Ste-Famille', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 1320)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 1320)

def test_auto_simulation_7():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 5, 38, 0), datetime(2017, 5, 1, 5, 55, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('5e avenue / de Verdun', 1)
    assert stats['max_end'] == ('de Maisonneuve / Robert-Bourassa', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 1020)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 1020)

def test_auto_simulation_8():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 14, 43, 0), datetime(2017, 5, 1, 14, 52, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Milton / Université', 4)
    assert stats['max_end'] == ('Clark / Guilbault', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 540)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 540)

def test_auto_simulation_9():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 16, 58, 0), datetime(2017, 5, 1, 16, 59, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Clark / Rachel', 1)
    assert stats['max_end'] == ('Bishop / Ste-Catherine', 1)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 60)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 60)

def test_auto_simulation_10():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 14, 43, 0), datetime(2017, 5, 1, 15, 29, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Milton / Université', 6)
    assert stats['max_end'] == ('Métro Mont-Royal (Rivard / du Mont-Royal)', 4)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 2760)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 2760)


if __name__ == '__main__':
    import pytest
    pytest.main(['autotest_10E.py'])
