# Datei zur konfiguration der Simulation
from engine_euler import *


erde = Objekt(masse=5.9724 * ykg)
mond = Objekt(masse=0.07346 * ykg, pos=np.array([0.3844 * mkm, 0., 0.]), v_vek=np.array([0., 1.022 * 1000, 0.]))


simulation(60, 27.3217 * 24 * 3600)

plt.show()
