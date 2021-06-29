# Datei zur konfiguration der Simulation
from engine_euler import *


sonne = Objekt(masse=1988500e24)
#erde = Objekt(masse=5.9724e24, r=np.array([147.092e9, 0., 0.]), v=np.array([0., 30.29e3, 0.]))
mars = Objekt(masse=0.64171e24, r=np.array([-206.617e9, 0., 0.]), v=np.array([0., -26.50e3, 0.]))

def main():
    import cProfile
    import pstats

    with cProfile.Profile() as pr:
        simulation(10 * 60, 1 * yr, "Sonne und Mars")

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats = stats
    stats.print_stats(10)

    print('End')

if __name__ == '__main__':
    main()
