# Datei zur konfiguration der Simulation
from engine_euler import *

sonnensystem = System(10 * 60, 1 * yr, "Sonnensystem")
sonne = Objekt(masse=1988500e24)
erde = Objekt(masse=5.9724e24, r=np.array([147.092e9, 0., 0.]), v=np.array([0., 30.29e3, 0.]))
mars = Objekt(masse=0.64171e24, r=np.array([206.617e9, 0., 0.]), v=np.array([0., 26.50e3, 0.]))
sonnensystem.objekt_hinzu(sonne)
sonnensystem.objekte.append(erde)
sonnensystem.objekte.append(mars)
#merkur = Objekt(masse=0.33011e24, r=np.array([46.002e9, 0., 0.]), v=np.array([0., 58.98e3, 0.]))
#venus = Objekt(masse=4.8675e24, r=np.array([107.476e9, 0., 0.]), v=np.array([0., 35.26e3, 0.]))
#jupiter = Objekt(masse=1898.19e24, r=np.array([740.522e9, 0., 0.]), v=np.array([0., 13.72e3, 0.]))
#saturn = Objekt(masse=568.34e24, r=np.array([1352.555e9, 0., 0.]), v=np.array([0., 10.18e3, 0.]))
#uranus = Objekt(masse=86.813e24, r=np.array([2741.302e9, 0., 0.]), v=np.array([0., 7.11e3, 0.]))
#neptun = Objekt(masse=102.413e24, r=np.array([4444.449e9, 0., 0.]), v=np.array([0., 5.50e3, 0.]))
#pluto = Objekt(masse=0.01303e24, r=np.array([7304.326e9, 0., 0.]), v=np.array([0., 3.71e3, 0.]))


def main():
    import cProfile
    import pstats

    with cProfile.Profile() as pr:
        sonnensystem.simulation()

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats = stats
    stats.print_stats(10)

    print('End')

if __name__ == '__main__':
    main()
