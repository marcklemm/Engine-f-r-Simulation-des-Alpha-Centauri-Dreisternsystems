# Datei zur konfiguration der Simulation
from engine import *

obj1 = Objekt(masse=1, pos=[0, 0, 15])
obj2 = Objekt(masse=1, pos=[1, 2, 3])
obj3 = Objekt(masse=1, pos=[2, 5, 3])


gravitation(obj1)
gravitation(obj2)
gravitation(obj3)
print(obj1.a_vek)
print(obj2.a_vek)
print(obj3.a_vek)