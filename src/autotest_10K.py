from datetime import datetime
import os
import pygame
from simulation import Simulation


def test_auto_simulation_1():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 18, 49, 0), datetime(2017, 5, 1, 18, 50, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Vallières / St-Dominique', 2)
    assert stats['max_end'] == ('Louis-Hébert / Bélanger', 1)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 60)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 60)

def test_auto_simulation_2():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 7, 59, 0), datetime(2017, 5, 1, 8, 12, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('de la Gauchetière / Robert-Bourassa', 2)
    assert stats['max_end'] == ('Marmier / St-Denis', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 780)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 780)

def test_auto_simulation_3():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 11, 30, 0), datetime(2017, 5, 1, 11, 58, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Jeanne-Mance / St-Viateur', 4)
    assert stats['max_end'] == ('Jeanne-Mance / St-Viateur', 4)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 1680)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 1680)

def test_auto_simulation_4():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 15, 30, 0), datetime(2017, 5, 1, 15, 56, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Métro Mont-Royal (Rivard / du Mont-Royal)', 4)
    assert stats['max_end'] == ('Marquette / du Mont-Royal', 4)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 1560)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 1560)

def test_auto_simulation_5():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 21, 28, 0), datetime(2017, 5, 1, 21, 33, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Dandurand / Papineau', 1)
    assert stats['max_end'] == ('1ère avenue / Masson', 1)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 300)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 300)

def test_auto_simulation_6():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 1, 52, 0), datetime(2017, 5, 1, 1, 57, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('10e Avenue / Rosemont', 0)
    assert stats['max_end'] == ('Rivard / Rachel', 1)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 300)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 300)

def test_auto_simulation_7():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 21, 47, 0), datetime(2017, 5, 1, 22, 43, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Mackay /de Maisonneuve (Sud)', 4)
    assert stats['max_end'] == ('Beaudry / Sherbrooke', 3)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 3360)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 3360)

def test_auto_simulation_8():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 21, 57, 0), datetime(2017, 5, 1, 21, 58, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Métro Joliette  (Joliette / Hochelaga)', 1)
    assert stats['max_end'] == ('Boyer / Rosemont', 1)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 60)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 60)

def test_auto_simulation_9():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 16, 2, 0), datetime(2017, 5, 1, 17, 27, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Milton / Clark', 11)
    assert stats['max_end'] == ('Gilford / Brébeuf', 6)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 5100)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 5100)

def test_auto_simulation_10():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 14, 5, 0), datetime(2017, 5, 1, 15, 21, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Milton / Université', 9)
    assert stats['max_end'] == ('Métro Mont-Royal (Rivard / du Mont-Royal)', 5)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 4560)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 4560)


if __name__ == '__main__':
    import pytest
    pytest.main(['autotest_10K.py'])
