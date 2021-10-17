# Datei zur konfiguration der Simulation
from engine_rk4 import * # zur Simulation mit Euler engine_euler verwenden

alpha_centauri = System(10*day , 15000*yr, "Alpha Centauri ABC", print_genauigkeit=4000) # Das System, welches berechnet werden soll

# die Objekte, welche simuliert werden sollen
alpha_centauri_a = Objekt(masse=1.0788 * solar_mass, r=np.array([-5.120328224503452 * ae, 0., 0.]), v=np.array([0.,-7076.646018735186, 0.]), obj_id="Alpha Centauri A")
alpha_centauri_b = Objekt(masse=0.9092 * solar_mass, r=np.array([6.0754620420087155 * ae, 0., 0.]), v=np.array([0., 8396.706692709546, 0.]), obj_id="Alpha Centauri B")

alpha_centauri_ab = Objekt(masse=(1.0788+0.9092) * solar_mass, obj_id="Alpha Centauri AB")

proxima_centauri = Objekt(masse=0.1221 * solar_mass, r=np.array([0., 5.3e3 * ae, 0.]), v=np.array([-686.91, 0., 0.]), obj_id="Proxima Centauri")

alpha_centauri.objekt_hinzu(alpha_centauri_a, alpha_centauri_b) # fügt die Körper dem System hinzu alpha_centauri_ab, proxima_centauri


def main():
    import cProfile
    import pstats

    with cProfile.Profile() as pr:
        # was gemessen werden soll -- für Berechnung Sonnensystem:  sonnensystem.simulation()
        alpha_centauri.simulation()
    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats = stats
    stats.print_stats(10)

    print('End')
    plt.show()

if __name__ == '__main__':
    main()

# es kann auch das Sonnensystem für die Simulation verwendet werden:
"""
sonnensystem = System(0.1 * day, 10  * yr, "Sonnensystem mit Pluto", print_genauigkeit=500)o

sonne = Objekt(masse=solar_mass, obj_id='Sonne')
erde = Objekt(masse=5.9724e24, r=np.array([147.092e9, 0., 0.]), v=np.array([0., 30.29e3, 0.]), obj_id='Erde')
mars = Objekt(masse=0.64171e24, r=np.array([206.617e9, 0., 0.]), v=np.array([0., 26.50e3, 0.]), obj_id='Mars')
merkur = Objekt(masse=0.33011e24, r=np.array([46.002e9, 0., 0.]), v=np.array([0., 58.98e3, 0.]), obj_id='Merkur')
venus = Objekt(masse=4.8675e24, r=np.array([107.476e9, 0., 0.]), v=np.array([0., 35.26e3, 0.]), obj_id='Venus')
jupiter = Objekt(masse=1898.19e24, r=np.array([740.522e9, 0., 0.]), v=np.array([0., 13.72e3, 0.]), obj_id='Jupiter')
saturn = Objekt(masse=568.34e24, r=np.array([1352.555e9, 0., 0.]), v=np.array([0., 10.18e3, 0.]), obj_id='Saturn')
uranus = Objekt(masse=86.813e24, r=np.array([2741.302e9, 0., 0.]), v=np.array([0., 7.11e3, 0.]), obj_id='Uranus')
neptun = Objekt(masse=102.413e24, r=np.array([4444.449e9, 0., 0.]), v=np.array([0., 5.50e3, 0.]), obj_id='Neptun')
pluto = Objekt(masse=0.01303e24, r=np.array([7304.326e9, 0., 0.]), v=np.array([0., 3.71e3, 0.]), obj_id='Pluto')

sonnensystem.objekt_hinzu(sonne, merkur, venus, erde, mars, jupiter, saturn, uranus, neptun) #, pluto
"""