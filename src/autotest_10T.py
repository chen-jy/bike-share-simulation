from datetime import datetime
import os
import pygame
from simulation import Simulation


def test_auto_simulation_1():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 17, 53, 0), datetime(2017, 5, 1, 18, 10, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Prince-Arthur / du Parc', 4)
    assert stats['max_end'] == ('Marquette / du Mont-Royal', 5)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 1020)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 1020)

def test_auto_simulation_2():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 14, 28, 0), datetime(2017, 5, 1, 15, 16, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Milton / Université', 6)
    assert stats['max_end'] == ('Métro Mont-Royal (Rivard / du Mont-Royal)', 5)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 2880)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 2880)

def test_auto_simulation_3():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 9, 59, 0), datetime(2017, 5, 1, 10, 38, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Métro Mont-Royal (Rivard / du Mont-Royal)', 3)
    assert stats['max_end'] == ('de la Commune / St-Sulpice', 3)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 2340)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 2340)

def test_auto_simulation_4():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 11, 56, 0), datetime(2017, 5, 1, 12, 37, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Métro Place-des-Arts (de Maisonneuve / de Bleury)', 3)
    assert stats['max_end'] == ('4e avenue / Masson', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 2460)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 2460)

def test_auto_simulation_5():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 14, 51, 0), datetime(2017, 5, 1, 14, 51, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Marie-Anne / de la Roche', 1)
    assert stats['max_end'] == ('10e Avenue / Rosemont', 0)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 60)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 60)

def test_auto_simulation_6():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 9, 57, 0), datetime(2017, 5, 1, 10, 57, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Métro Bonaventure (de la Gauchetière / Mansfield)', 3)
    assert stats['max_end'] == ('de la Commune / St-Sulpice', 3)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 3600)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 3600)

def test_auto_simulation_7():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 13, 36, 0), datetime(2017, 5, 1, 13, 59, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Milton / Clark', 2)
    assert stats['max_end'] == ('de la Commune / Berri', 3)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 1380)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 1380)

def test_auto_simulation_8():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 18, 11, 0), datetime(2017, 5, 1, 18, 24, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Maguire / Henri-Julien', 3)
    assert stats['max_end'] == ('Dorion / Ontario', 3)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 780)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 780)

def test_auto_simulation_9():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 6, 26, 0), datetime(2017, 5, 1, 6, 47, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Benny / de Monkland', 2)
    assert stats['max_end'] == ('Métro Mont-Royal (Rivard / du Mont-Royal)', 2)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 1260)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 1260)

def test_auto_simulation_10():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    sim = Simulation('stations.json', 'custom_rides_1.csv')
    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
    sim.run(datetime(2017, 5, 1, 7, 59, 0), datetime(2017, 5, 1, 7, 59, 0))
    stats = sim.calculate_statistics()
    assert stats['max_start'] == ('Berri / Cherrier', 1)
    assert stats['max_end'] == ('10e Avenue / Rosemont', 0)
    assert stats['max_time_low_availability'] == ('15e avenue / Masson', 60)
    assert stats['max_time_low_unoccupied'] == ('10e Avenue / Rosemont', 60)


if __name__ == '__main__':
    import pytest
    pytest.main(['autotest_10T.py'])
