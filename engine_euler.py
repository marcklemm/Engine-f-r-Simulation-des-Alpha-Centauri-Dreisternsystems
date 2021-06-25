import numpy as np
import json
import matplotlib.pyplot as plt

'''Konstanten'''
G = 6.67430e-11

'''Einheiten'''
ykg = 10e24 # yotta kg
mkm = 10e9 # mega km

'''Objekt-Array'''
objekte = []

'''Funktionen'''


def sqrt(x):
    # berechnet die Wurzel
    return x**0.5


def sq(x):
    # berechnet das Quadrat
    return x**2


'''Simulation'''


class Objekt:
    def __init__(self, masse=1, pos=np.array([0., 0., 0.]), a_vek=np.array([0., 0., 0.]), v_vek=np.array([0., 0., 0.])):
        self.masse = masse
        self.pos = pos
        self.a_vek = a_vek
        self.v_vek = v_vek
        objekte.append(self)


def gravitation(obj1, obj2):
    richtungs_vek = np.array([0., 0., 0.])

    '''Differenz der Vektoren -> Richtungsvektor'''
    for i in range(0, 3):
        richtungs_vek[i] = obj2.pos[i]-obj1.pos[i]

    '''Betrag des Vektors'''
    betrag = sqrt(sq(richtungs_vek[0]) + sq(richtungs_vek[1]) + sq(richtungs_vek[2]))

    '''Beschleunigungsvektor'''
    for i in range(0, 3):
        obj1.a_vek[i] = - G * obj2.masse/betrag**3 * richtungs_vek[i]

def result(pos1, pos2):
    x = 0
    print(pos1, pos2)
    for i in range(0, 3):
         x += sqrt(sq(pos2[i]-pos1[i]))
    return x


def simulation(dt, t):
    vergangene_t = 0
    anfangs_vek = np.array([x for x in objekte[1].pos])
    print(anfangs_vek)
    while vergangene_t <= t:

        '''berechnet die Position aller Objekte'''
        for obj1 in objekte:
            ax.scatter(obj1.pos[0], obj1.pos[1], obj1.pos[2])
            for obj2 in objekte:
                if obj1 != obj2:
                    gravitation(obj1, obj2)
        print(vergangene_t, 'Erde: ', objekte[0].pos, 'Mond: ', objekte[1].pos)

        for obj in objekte:

            '''berechnet die Position nach dt'''
            for i in range(0, 3):
                obj.pos[i] += obj.v_vek[i] * dt + 0.5 * obj.a_vek[i] * sq(dt)

            '''berechnet den Geschwindigkeits Vektor'''
            for i in range(0, 3):
                obj.v_vek[i] += obj.a_vek[i] * dt
        vergangene_t += dt
    print(result(anfangs_vek, objekte[1].pos))


def output(data, output_file):
    with open(output_file, 'a') as log:
        json.dump(data, log, indent=len(data), separators=(',', ':'))


fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot(111, projection='3d')
