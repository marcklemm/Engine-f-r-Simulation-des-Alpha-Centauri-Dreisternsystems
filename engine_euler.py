# In dieser Datei sind alle Funktionen beinhaltet, welche in main.py benötigt werden.
# Konstanten
g = 1

# Objekt-Array
objekte = []

# Variabeln
richtungs_vek = [0, 0, 0]
betrag_vek = [0, 0, 0]
dt = 1


class Objekt:
    def __init__(self, masse=1, pos=[0, 0, 0], a_vek=[0, 0, 0], v_vek=[0, 0, 0], id=""):
        self.masse = masse
        self.pos = pos
        self.a_vek = a_vek
        self.v_vek = v_vek
        self.id = id
        objekte.append(self) # fügt Objekt in "objekte" ein

# Funktionen
def gravitation(obj1, obj2):
    for i in range(0, 3): # Differenz der Vektoren
        richtungs_vek[i] = obj2.pos[i]-obj1.pos[i]
    betrag_vek = (richtungs_vek[0]**2 + richtungs_vek[1]**2 + richtungs_vek[2]**2)**(0.5*3) # Betrag des Vektors und hoch 3
    for i in range(0, 3): # Beschleunigungsvektor
        obj1.a_vek[i] = -g * (obj2.masse)/(betrag_vek) * richtungs_vek[i]

def pos_update():
    for obj in objekte:
        for i in range(0, 3):
            obj.pos[i] += obj.v_vek[i] * dt + 0.5 * obj.a_vek[i] * dt**2
        for i in range(0, 3):
            obj.v_vek[i] += obj.a_vek[i] * dt

def simulation(t):
    vergangene_t = 0
    while vergangene_t <= t:
        for obj1 in objekte:
            for obj2 in objekte:
                if obj1 != obj2:
                    gravitation(obj1, obj2)
            print(vergangene_t, obj1.id, obj1.pos)
        pos_update()
        vergangene_t += dt

