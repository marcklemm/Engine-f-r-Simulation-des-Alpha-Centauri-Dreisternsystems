# Datei zur konfiguration der Simulation
from engine_euler import *


erde = Objekt(masse=5.9722e24, name="Erde")
mond = Objekt(masse=7.342e22, name="Mond", pos=np.array([0.4055e6, 0, 0]), v_vek=np.array([0, 970, 0]))


simulation(10, 60 * 60)

plt.show()
