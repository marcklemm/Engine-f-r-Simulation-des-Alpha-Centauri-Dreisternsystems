# Datei zur konfiguration der Simulation
from engine_rk4 import *

sonnensystem = System(600, 42 * yr, "Sonnensystem mit Pluto")

sonne = Objekt(masse=1988500e24)
erde = Objekt(masse=5.9724e24, r=np.array([147.092e9, 0., 0.]), v=np.array([0., 30.29e3, 0.]), obj_id='Erde')
mars = Objekt(masse=0.64171e24, r=np.array([206.617e9, 0., 0.]), v=np.array([0., 26.50e3, 0.]), obj_id='Mars')
merkur = Objekt(masse=0.33011e24, r=np.array([46.002e9, 0., 0.]), v=np.array([0., 58.98e3, 0.]), obj_id='Merkur')
venus = Objekt(masse=4.8675e24, r=np.array([107.476e9, 0., 0.]), v=np.array([0., 35.26e3, 0.]), obj_id='Venus')
jupiter = Objekt(masse=1898.19e24, r=np.array([740.522e9, 0., 0.]), v=np.array([0., 13.72e3, 0.]), obj_id='Jupiter')
saturn = Objekt(masse=568.34e24, r=np.array([1352.555e9, 0., 0.]), v=np.array([0., 10.18e3, 0.]), obj_id='Saturn')
uranus = Objekt(masse=86.813e24, r=np.array([2741.302e9, 0., 0.]), v=np.array([0., 7.11e3, 0.]), obj_id='Uranus')
neptun = Objekt(masse=102.413e24, r=np.array([4444.449e9, 0., 0.]), v=np.array([0., 5.50e3, 0.]), obj_id='Neptun')
pluto = Objekt(masse=0.01303e24, r=np.array([7304.326e9, 0., 0.]), v=np.array([0., 3.71e3, 0.]), obj_id='Pluto')

sonnensystem.objekt_hinzu(sonne, merkur, venus, erde, mars, jupiter, saturn, uranus, neptun, pluto)


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
    plt.show()


if __name__ == '__main__':
    main()
