import numpy as np
import json
import matplotlib.pyplot as plt

'''Konstanten'''
G = 6.67430e-11


"""Funkationen"""


def betrag(vek):
    return np.sqrt(np.sum(vek**2))


'''Simulation'''


fig = plt.figure(figsize=(10, 10))

objekte = [] # beinhaltet die zu simulierenden Objekte


def exzentrizitaet(obj):
    apphelion = max(obj.abstand)
    perihelion = min(obj.abstand)
    print(apphelion, perihelion)
    exzent = (apphelion-perihelion)/(apphelion+perihelion)
    return exzent


class Objekt:
    def __init__(self, masse=1, pos=np.array([0., 0., 0.]), a_vek=np.array([0., 0., 0.]), v_vek=np.array([0., 0., 0.])):
        self.masse = masse
        self.pos = pos
        self.a_vek = a_vek
        self.v_vek = v_vek
        self.coordinates = [[], [], []]
        self.abstand = []
        self.ax = fig.add_subplot(111, projection='3d')
        objekte.append(self)

    def abstand_zu_stern(self):
        self.abstand.append(betrag(self.pos - objekte[0].pos))


def gravitation(obj1, obj2):
    richtungs_vek = obj2.pos-obj1.pos
    abstand = betrag(richtungs_vek)
    obj1.a_vek = G * obj2.masse/abstand**3 * richtungs_vek


def simulation(dt, t):
    vergangene_t = 0
    while vergangene_t <= t:
        for obj in objekte:
            obj.pos += obj.v_vek * dt + 0.5 * obj.a_vek * dt**2 # berechnet die Position aller Objekte
            obj.v_vek += obj.a_vek * dt # berechnet die Geschwindigkeit der Objekte
            for i in range(3):
                obj.coordinates[i].append(objekte[1].pos[i])
            obj.abstand_zu_stern()
            for obj1 in objekte: # berechnet die Beschleunigungen der Objekte
                for obj2 in objekte:
                    if obj1 != obj2:
                        gravitation(obj1, obj2)
        vergangene_t += dt
    for obj in objekte:
        obj.ax.scatter(obj.coordinates[0], obj.coordinates[1], obj.coordinates[2])
    print(exzentrizitaet(objekte[1]))
    plt.show()


def output(data, output_file):
    with open(output_file, 'a') as log:
        json.dump(data, log, indent=len(data), separators=(',', ':'))
