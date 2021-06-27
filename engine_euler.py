import numpy as np
import json
import matplotlib.pyplot as plt

'''Konstanten'''
G = 6.67430e-11


'''Simulation'''


fig = plt.figure(figsize=(4, 4))

objekte = [] # beinhaltet die zu simulierenden Objekte


class Objekt:
    def __init__(self, masse=1, pos=np.array([0., 0., 0.]), a_vek=np.array([0., 0., 0.]), v_vek=np.array([0., 0., 0.])):
        self.masse = masse
        self.pos = pos
        self.a_vek = a_vek
        self.v_vek = v_vek
        self.ax = fig.add_subplot(111, projection='3d')
        objekte.append(self)


def gravitation(obj1, obj2):
    richtungs_vek = np.array([0., 0., 0.])
    richtungs_vek = obj2.pos-obj1.pos
    betrag = np.sqrt(np.sum(richtungs_vek**2))
    obj1.a_vek = G * obj2.masse/betrag**3 * richtungs_vek


def simulation(dt, t):
    coordinates = [[], [], []]
    vergangene_t = 0
    while vergangene_t <= t:
        for obj in objekte:
            obj.pos += obj.v_vek * dt + 0.5 * obj.a_vek * dt**2
            obj.v_vek += obj.a_vek * dt
            for i in range(3):
                coordinates[i].append(objekte[1].pos[i])
            for obj1 in objekte: # berechnet die Position aller Objekte
                for obj2 in objekte:
                    if obj1 != obj2:
                        gravitation(obj1, obj2)
        vergangene_t += dt
    for obj in objekte:
        obj.ax.scatter(coordinates[0], coordinates[1], coordinates[2])
    plt.show()


def output(data, output_file):
    with open(output_file, 'a') as log:
        json.dump(data, log, indent=len(data), separators=(',', ':'))
