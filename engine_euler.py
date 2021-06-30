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
    return np.sqrt(sum(vek**2))


'''Simulation'''
class System:
    def __init__(self, dt, t, name, output_file="log.json"):
        self.objekte = []
        self.dt = dt
        self.t = t
        self.name = name
        self.output_file = output_file

    def objekt_hinzu(self, *args):
        for arg in args:
            self.objekte.append(arg)

    def gravitation(self):
        for i, obj1 in enumerate(self.objekte):
            for obj2 in self.objekte[i + 1:]:
                richtungs_vek = obj2.r - obj1.r
                f = G * obj2.masse * obj1.masse / betrag(richtungs_vek) ** 3 * richtungs_vek
                obj1.a += f / obj1.masse
                obj2.a += -1 * f /obj2.masse


    def r_update(self):
        self.abstand_zu_stern()
        for obj in self.objekte:
            obj.r += obj.v * self.dt + 0.5 * obj.a * self.dt ** 2  # berechnet die Position aller Objekte
            obj.coordinates.append(obj.r.tolist())
            obj.v += obj.a * self.dt  # berechnet die Geschwindigkeit der Objekte

    def abstand_zu_stern(self):
        for obj in self.objekte:
            obj.abstand.append(betrag(obj.r - self.objekte[0].r))

    def simulation(self):
        vergangene_t = 0
        fig = plt.figure(figsize=(10, 10), tight_layout=True)
        ax = fig.add_subplot(projection='3d')
        while vergangene_t <= self.t:
            for obj in self.objekte:
                obj.a = [0, 0, 0]
                obj.r_aufteilen()
                ax.scatter(obj.xs, obj.ys)
            self.gravitation()  # berechnet die Beschleunigungen der Objekte
            self.r_update()
            vergangene_t += self.dt
        data = {"Name": self.name, "dt": self.dt, "t": self.t}
        for obj in self.objekte[1:]:
            data[f'Exzentrizitaet {obj.obj_id}'] = f'{obj.exzentrizitaet()}'
            data[f'Umlaufdauer {obj.obj_id}'] = f'{obj.umlaufdauer}'
        self.output(data)

    def output(self, data):
        with open(self.output_file, 'r+') as log:
            content = json.load(log)
            content.append(data)
            log.seek(0)
            json.dump(content, separators=(',', ':'), fp=log, indent=len(data))
            log.truncate()


class Objekt:
    def __init__(self, masse=1, a=np.array([0., 0., 0.]), v=np.array([0., 0., 0.]), r=np.array([0., 0., 0.]), obj_id='objekt'):
        self.masse = masse
        self.a = a
        self.v = v
        self.r = r
        self.obj_id = obj_id

        self.coordinates = []
        self.xs = []
        self.ys = []
        self.zs = []
        self.abstand = []

    def r_aufteilen(self):
        self.xs += [r[0] for r in self.coordinates]
        self.ys += [r[1] for r in self.coordinates]
        self.zs += [r[2] for r in self.coordinates]

    def exzentrizitaet(self):
        apphelion = max(self.abstand)
        perihelion = min(self.abstand)
        print(apphelion, perihelion)
        exzent = (apphelion - perihelion) / (apphelion + perihelion)
        return exzent
