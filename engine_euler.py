import matplotlib.pyplot as plt
import json
# In dieser Datei sind alle Funktionen beinhaltet, welche in main.py benötigt werden.
# Konstanten
g = - 6.67430e-11

# Objekt-Array
objekte = []

# Variabeln
dt = 0.01


class Objekt:
    def __init__(self, masse=1, pos=[0, 0, 0], a_vek=[0, 0, 0], v_vek=[0, 0, 0]):
        self.masse = masse
        self.pos = pos
        self.a_vek = a_vek
        self.v_vek = v_vek

        # fügt Objekt in "objekte" ein
        objekte.append(self)

# Funktionen


def gravitation(obj1, obj2):
    richtungs_vek = [0, 0, 0]
    betrag_vek = [0, 0, 0]

    # Differenz der Vektoren
    for i in range(0, 3):
        richtungs_vek[i] = obj2.pos[i]-obj1.pos[i]

    # Betrag des Vektors und hoch 3
    betrag_vek = (richtungs_vek[0]**2 + richtungs_vek[1]**2 + richtungs_vek[2]**2)**(0.5*3)

    # Beschleunigungsvektor
    for i in range(0, 3):
        obj1.a_vek[i] = - g * (obj2.masse)/(betrag_vek) * richtungs_vek[i]



def pos_update():
    for obj in objekte:

        # berechnet die Position nach dt
        for i in range(0, 3):
            obj.pos[i] += obj.v_vek[i] * dt + 0.5 * obj.a_vek[i] * dt**2

        # berechnet den Geschwindigkeits Vektor
        for i in range(0, 3):
            obj.v_vek[i] += obj.a_vek[i] * dt


def simulation(t):
    vergangene_t = 0
    while vergangene_t <= t:

        # berechnet die Position aller Objekte
        for obj1 in objekte:
            ax.scatter(obj1.pos[0], obj1.pos[1], obj1.pos[2])
            for obj2 in objekte:
                if obj1 != obj2:
                    gravitation(obj1, obj2)
            print(vergangene_t, obj1.pos)

        pos_update()
        vergangene_t += dt


def output(data, output_file):
    with open(output_file, 'a') as log:
        json.dump(data, log, indent = len(data), seperators=',')


fig = plt.figure(figsize=(4,4))
ax = fig.add_subplot(111, projection='3d')
fig = plt.figure(figsize=(4,4))
ax = fig.add_subplot(111, projection='3d')