import numpy as np
import json
import matplotlib.pyplot as plt

'''Konstanten'''
G = 6.67430e-11


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

objekte = [] # beinhaltet die zu simulierenden Objekte




class Objekt:
    def __init__(self, masse=1, pos=np.array([0., 0., 0.]), a_vek=np.array([0., 0., 0.]), v_vek=np.array([0., 0., 0.])):
        self.masse = masse
        self.pos = pos
        self.a_vek = a_vek
        self.v_vek = v_vek
        self.x = []
        self.y = []
        self.z = []
        self.abstand = []
        self.ax = fig.add_subplot(111, projection='3d')
        objekte.append(self)

    def abstand_zu_stern(self):
        self.abstand.append(betrag(self.pos - objekte[0].pos))

    def pos_update(self):
        self.x.append(self.pos[0])
        self.y.append(self.pos[1])
        self.z.append(self.pos[2])


def gravitation(obj1, obj2):
    richtungs_vek = obj2.pos-obj1.pos
    abstand = betrag(richtungs_vek)
    obj1.a_vek = G * obj2.masse/abstand**3 * richtungs_vek


def simulation(dt, t, name=""):
    vergangene_t = 0
    while vergangene_t <= t:
        for obj in objekte:
            obj.pos += obj.v_vek * dt + 0.5 * obj.a_vek * dt**2 # berechnet die Position aller Objekte
            obj.pos_update()
            obj.v_vek += obj.a_vek * dt # berechnet die Geschwindigkeit der Objekte
            obj.abstand_zu_stern()
            for obj1 in objekte: # berechnet die Beschleunigungen der Objekte
                for obj2 in objekte:
                    if obj1 != obj2:
                        gravitation(obj1, obj2)
        vergangene_t += dt
    for obj in objekte:
        obj.ax.scatter(obj.x, obj.y, obj.z)
    output({"Name": name, "dt": dt, "t": t, "exzentrizitaet Erde": exzentrizitaet(objekte[1])}, 'log.json')
    plt.show()



