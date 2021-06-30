# In dieser Datei sind alle Funktionen beinhaltet, welche in main.py benötigt werden.
# Konstanten
g = 1

# Objekt-Array
objekte = []

# Variabeln
richtungs_vek = [0, 0, 0]
betrag_vek = [0, 0, 0]
dt = 0.1

# Objekte
class Objekt:
    def __init__(self, masse=1, pos=[0, 0, 0], a_vek=[0, 0, 0], v_vek=[0, 0, 0], temp_pos=[0, 0, 0], temp_a_vek=[0, 0, 0]):
        self.masse = masse
        self.pos = pos
        self.a_vek = a_vek
        self.v_vek = v_vek
        self.temp_pos = temp_pos
        self.temp_a_vek = temp_a_vek
        objekte.append(self) # fügt Objekt in "system" ein

    def zero(self):
        self.a_vek = [0, 0, 0]

    def berechnen_temp_pos(self, x):
        self.temp_pos = [0, 0, 0]
        for i in range(0, 3):
            self.temp_pos[i] = self.pos[i] + x[i]

    def berechnen_temp_a_vek(self, temp_pos):
        pass



# Funktionen
def gravitation(obj1, obj2, output="a_vek"):
    for i in range(0, 3): # Differenz der Vektoren
        richtungs_vek[i] = obj2.pos[i]-obj1.pos[i]
    betrag_vek = (richtungs_vek[0]**2 + richtungs_vek[1]**2 + richtungs_vek[2]**2)**(0.5*3) # Betrag des Vektors und hoch 3
    if output == "a_vek":
        for i in range(0, 3): # a_vek -> Beschleunigungsvektor
            obj1.a_vek[i] = -g * (obj2.masse)/(betrag_vek) * richtungs_vek[i]
    if output == "temp_a_vek":
        for i in range(0, 3): # temp_a_vek -> temporärer Beschleunigungsvektor
            obj1.temp_a_vek[i] = -g * (obj2.masse)/(betrag_vek) * richtungs_vek[i]


def beschleunigung_an_pos(obj): # addiert alle Beschleunigungen
    for objekt in objekte:
        if objekt != obj:
            gravitation(obj, objekt)
        else:
            pass

def position_nach_dt(obj):
    k0 = [0, 0, 0]
    l0 = [0, 0, 0]
    k1 = [0, 0, 0]
    l1 = [0, 0, 0]
    x1 = [0, 0, 0]
    k2 = [0, 0, 0]
    l2 = [0, 0, 0]
    x2 = [0, 0, 0]
    for i in range(0, 3):
        k0[i] = dt * obj.v_vek[i]
        l0[i] = dt * obj.a_vek[i]
        x1[i] = 0.5 * k0[i]
    obj.berechnen_temp_pos(x1)
    obj.berechnen_temp_a_vek()
    for i in range(0, 3):
        k1[i] = dt * (obj.v_vek[i] + 0.5 * l0[i])
        l1[i] = dt * (obj.temp_pos[i])
        x2[i] = 0.5 * k1[i]
    obj.berechnen_temp_pos(x2)
    for i in range(0, 3):
        k2[i] = dt * (obj.v_vek[i] * 0.5 * l1[i])
        l2[i] = dt * (obj.temp_pos[i])


