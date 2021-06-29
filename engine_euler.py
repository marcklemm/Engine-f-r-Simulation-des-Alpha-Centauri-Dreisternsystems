import numpy as np
import json
import matplotlib.pyplot as plt

'''Konstanten'''
G = 6.67430e-11


"""EInheiten"""
yr = 365 * 24 * 3600


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
fig = plt.figure(figsize=(10, 10)) # für matplot Simulation
ax = fig.add_subplot(111)

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

    def gravitation(self):
        for obj in objekte:
            if obj != self:
                richtungs_vek = obj.r - self.r
                abstand = betrag(richtungs_vek)
                self.a = G * obj.masse / abstand ** 3 * richtungs_vek


def simulation(dt, t, name=""):
    vergangene_t = 0
    while vergangene_t <= t:
        for obj in objekte:
            obj.abstand_zu_stern()
            obj.gravitation() # berechnet die Beschleunigungen der Objekte
            obj.r += obj.v * dt + 0.5 * obj.a * dt ** 2  # berechnet die Position aller Objekte
            obj.coordinates.append([r for r in obj.r])
            obj.v += obj.a * dt  # berechnet die Geschwindigkeit der Objekte
        vergangene_t += dt
    for obj in objekte:
        obj.r_update()
        ax.scatter(obj.x, obj.y)
    #output({"Name": name, "dt": dt, "t": t, "exzentrizitaet Mars": exzentrizitaet(objekte[1])}, 'log.json')
    plt.show()



