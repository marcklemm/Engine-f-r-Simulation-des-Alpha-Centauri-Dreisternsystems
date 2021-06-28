# Datei zur konfiguration der Simulation
from engine_euler import *


sonne = Objekt(masse=1988500e24)
erde = Objekt(masse=5.9724e24, pos=np.array([147.092e9, 0., 0.]), v_vek=np.array([0., 30.29e3, 0.]))
# jupiter = Objekt(masse=1898.19e24, pos=np.array([778.570e9, 0., 0.]), v_vek=np.array([0., 13.06e3, 0.]))

def main():
    import cProfile
    import pstats

    with cProfile.Profile() as pr:
        simulation(10 * 60, 1 * 365 * 24 * 3600, "Erde, Sonne und Jupiter")

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats = stats
    stats.print_stats(10)

    print('End')

if __name__ == '__main__':
    main()
