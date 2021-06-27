# Datei zur konfiguration der Simulation
from engine_euler import *


erde = Objekt(masse=5.9724 * ykg)
mond = Objekt(masse=0.07346 * ykg, pos=np.array([0.3844 * mkm, 0., 0.]), v_vek=np.array([0., 1.022 * km, 0.]))


def main():
    import cProfile
    import pstats

    with cProfile.Profile() as pr:
        simulation(60 * 10, 27.4 * 24 * 3600)

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()
    stats.dump_stats(filename='main.prof')

if __name__ == '__main__':
    main()