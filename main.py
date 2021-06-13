# Datei zur konfiguration der Simulation
from engine_euler import *

objekt1 = Objekt(masse=1, pos=[0, 0, 15], id= "n1")
objekt2 = Objekt(masse=1, pos=[1, 2, 5], id="n2")
objekt3 = Objekt(masse=1, pos=[2, 5, 3], id="n3")
simulation(100)