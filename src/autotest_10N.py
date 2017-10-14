from datetime import datetime
import os
import pygame
from simulation import Simulation


def test_auto_simulation_1():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 21, 38, 0), datetime(2017, 5, 1, 22, 34, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Mackay /de Maisonneuve (Sud)', 4)
    assert stats['max_end'] == ('Beaudry / Sherbrooke', 3)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 3360)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 3360)

def test_auto_simulation_2():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 16, 17, 0), datetime(2017, 5, 1, 17, 42, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Milton / Université', 12)
    assert stats['max_end'] == ('Berri / de Maisonneuve', 8)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 5100)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 5100)

def test_auto_simulation_3():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 0, 35, 0), datetime(2017, 5, 1, 1, 41, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Berri / St-Grégoire', 2)
    assert stats['max_end'] == ('du Mont-Royal / Clark', 3)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 3960)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 3960)

def test_auto_simulation_4():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 9, 19, 0), datetime(2017, 5, 1, 10, 56, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Métro Mont-Royal (Rivard / du Mont-Royal)', 4)
    assert stats['max_end'] == ('Métro St-Laurent (de Maisonneuve / St-Laurent)', 5)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 5820)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 5820)

def test_auto_simulation_5():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 14, 39, 0), datetime(2017, 5, 1, 14, 48, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Milton / Université', 3)
    assert stats['max_end'] == ('St-Alexandre / Ste-Catherine', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 540)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 540)

def test_auto_simulation_6():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 8, 54, 0), datetime(2017, 5, 1, 8, 56, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Guillaume Couture/Earnscliffe', 2)
    assert stats['max_end'] == ('Clark / Guilbault', 1)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 120)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 120)

def test_auto_simulation_7():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 19, 49, 0), datetime(2017, 5, 1, 19, 58, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Métro Laurier (Rivard / Laurier)', 3)
    assert stats['max_end'] == ('Champlain / Ontario', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 540)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 540)

def test_auto_simulation_8():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 4, 1, 0), datetime(2017, 5, 1, 5, 50, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('du Parc-La Fontaine / Roy', 2)
    assert stats['max_end'] == ('Berri / de Maisonneuve', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 6540)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 6540)

def test_auto_simulation_9():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 4, 3, 0), datetime(2017, 5, 1, 4, 20, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Métro Mont-Royal (Rivard / du Mont-Royal)', 1)
    assert stats['max_end'] == ('Métro George-Vanier (St-Antoine / Canning)', 1)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 1020)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 1020)

def test_auto_simulation_10():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 1, 2, 0), datetime(2017, 5, 1, 2, 15, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Berri / St-Grégoire', 2)
    assert stats['max_end'] == ('Prince-Arthur / Ste-Famille', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 4380)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 4380)


if __name__ == '__main__':
    import pytest
    pytest.main(['autotest_10N.py'])
