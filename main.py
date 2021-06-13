# Datei zur konfiguration der Simulation
from engine_euler import *


erde = Objekt(masse=5.9722e24, pos=[0, 0, 0])
mond = Objekt(masse=7.342e22, pos=[0.4055e6, 0, 0], v_vek=[0, 970, 0])


simulation(10)

plt.show()

