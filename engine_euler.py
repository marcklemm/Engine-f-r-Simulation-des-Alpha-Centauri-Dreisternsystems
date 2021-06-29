import numpy as np
import json
import matplotlib.pyplot as plt

'''Konstanten'''
G = 6.67430e-11


"""EInheiten"""
yr = 365 * 24 * 3600
d = 24 * 365

"""Funktionen"""
def betrag(vek):
    return np.sqrt(np.sum(vek**2))


def exzentrizitaet(obj):
    apphelion = max(obj.abstand)
    perihelion = min(obj.abstand)
    print(apphelion, perihelion)
    exzent = (apphelion-perihelion)/(apphelion+perihelion)
    return exzent


def output(data, output_file):
    with open(output_file, 'a') as log:
        json.dump(data, log, indent=len(data), separators=(',', ':'))

'''Simulation'''
fig, ax = plt.subplots(figsize=(10, 10), tight_layout=True)


objekte = [] # beinhaltet die zu simulierenden Objekte


class Objekt:
    def __init__(self, masse=1, a=np.array([0., 0., 0.]), v=np.array([0., 0., 0.]), r=np.array([0., 0., 0.])):
        self.masse = masse
        self.a = a
        self.v = v
        self.r = r
        self.coordinates = []
        self.x = []
        self.y = []
        self.z = []
        self.abstand = []
        objekte.append(self)

    def abstand_zu_stern(self):
        self.abstand.append(betrag(self.r - objekte[0].r))

    def r_update(self):
        self.x += [r[0] for r in self.coordinates]
        self.y += [r[1] for r in self.coordinates]
        self.z += [r[2] for r in self.coordinates]


def gravitation():
    for i, obj1 in enumerate(objekte):
            for obj2 in objekte[i+1:]:
                richtungs_vek = obj2.r - obj1.r
                abstand = betrag(richtungs_vek)
                f = G * obj2.masse * obj1.masse / abstand ** 3 * richtungs_vek
                obj1.a = f / obj1.masse
                obj2.a = - f / obj2.masse


def simulation(dt, t, name=""):
    vergangene_t = 0
    while vergangene_t <= t:
        gravitation()  # berechnet die Beschleunigungen der Objekte
        for obj in objekte:
            obj.abstand_zu_stern()
            obj.r += obj.v * dt + 0.5 * obj.a * dt ** 2  # berechnet die Position aller Objekte
            obj.coordinates.append([r for r in obj.r])
            obj.v += obj.a * dt  # berechnet die Geschwindigkeit der Objekte
        vergangene_t += dt
    for obj in objekte:
        obj.r_update()
        ax.scatter(obj.x, obj.y)
    #output({"Name": name, "dt": dt, "t": t, "exzentrizitaet Mars": exzentrizitaet(objekte[1])}, 'log.json')
    plt.show()



