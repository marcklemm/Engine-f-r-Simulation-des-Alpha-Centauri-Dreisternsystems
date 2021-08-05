# Diese Variation der Simulation approximiert die Bewegung der Körper in einem System basierend auf dem Runge-Kutta-
# Verfahren 4. Ordnung. Dieses Verfahren ist im Vergleich zu anderen Methoden enorm präzise und dies auch über mehr
# Iterationen. Allerdings folgt aus dieser exakteren Methode auch, dass die Berechnungen länger dauert.

import numpy as np
import json
import matplotlib.pyplot as plt

'''Konstanten'''
G = 6.67430e-11 # Gravitationskonstante
pi = 3.1415926535 # Kreiszahl pi
ae =  1.495978707e11 # Astronomische Einheit
solar_mass = 1.989e30

"""Einheiten"""
yr = 365 * 24 * 3600 # Jahr in Sekunden
d = 24 * 3600 # Tag in Sekunden

"""Funktionen"""
def betrag(vek): # berechnet Betrag eines Vektors (Numpy Array)
    return np.sqrt(sum(vek**2))

'''Simulation'''
fig = plt.figure(figsize=(10, 10), tight_layout=True)
ax = fig.add_subplot(projection='3d')

# System, in welchem sich die Körper bewegen
class System:

    def __init__(self, dt, t, name, print_genauigkeit, output_file="log.json", output_koords='koordinaten.txt'):
        self.objekte = [] # enthält alle Körper, welche sich im System befinden
        self.dt = dt # Zeitintervall
        self.t = t # Gesamtzeit der Simulation
        self.name = name # Name zur Identifikation der Simulation
        self.output_file = output_file # Datei, in welche relevante Informationen über die Simulation gespeichert werden
        self.output_koords = output_koords
        self.print_genauigkeit = print_genauigkeit
        self.vergangene_t = 0
        if print_genauigkeit and print_genauigkeit > 1:
            schritt = np.arange(0, self.t + self.dt, self.dt, dtype='int')
            self.schritt = [x for i, x in enumerate(schritt) if i % (len(schritt) // (self.print_genauigkeit-1)) == 0]
        else:
            self.schritt = np.arange(0, self.t + self.dt, self.dt, dtype='int')

    # fügt alle Körper, welche für die Simulation verwendet werden sollen zum System hinzu
    def objekt_hinzu(self, *args):
        for arg in args:
            self.objekte.append(arg)

    # berechnet die Beschleunigung aus den Positionen und Masse der Objekte im System
    def gravitation_rk4(self, r, obj1):
        for i, obj in enumerate(self.objekte): # vergleicht alle Objekte mit der angegebenen Position
            if obj != obj1: # die Berechnung wird durchgeführt, wenn das Objekt sich nicht mit sich selber vergleicht
                richtungs_vek = obj.r - r # berechnet den Richtungsvektor zwischen r und obj.r
                differenz = betrag(richtungs_vek) # berechnet den Abstand zwischen r und obj.r

                # ändert Apsis und Perapsis + Halbachse
                if i == 0:
                    if obj1.perihel == 0:
                        obj1.perihel = differenz
                        obj1.semi_ax_up()
                    if differenz <= obj1.perihel:
                        obj1.perihel = differenz
                        obj1.semi_ax_up()
                    if differenz >= obj1.apphel:
                        obj1.apphel = differenz
                        obj1.semi_ax_up()


                return G * obj.masse / differenz ** 3 * richtungs_vek # die Beschleunigung wird berechnet

    # berechnet die Geschwindigkeit, sowie die Position der Körper nach dem Runge-Kutta-Verfahren 4. Ordnung
    def r_update_rk4(self):
        for obj in self.objekte:
            k0 = self.dt * obj.v
            l0 = self.dt * self.gravitation_rk4(obj.r, obj)

            k1 = self.dt * (obj.v + .5 * l0)
            l1 = self.dt * self.gravitation_rk4(obj.r + .5 * k0, obj)

            k2 = self.dt * (obj.v + .5 * l1)
            l2 = self.dt * self.gravitation_rk4(obj.r + .5 * k1, obj)

            k3 = self.dt * (obj.v + .5 * l2)
            l3 = self.dt * self.gravitation_rk4(obj.r + .5 * k2, obj)

            obj.r += (1/6) * (k0 + 2 * k1 + 2 * k2 + k3) # ändert die berechnete Position des Körpers
            obj.v += (1/6) * (l0 + 2 * l1 + 2 * l2 + l3) # ändert die berechnete Geschwindigkeit des Körpers

            if self.vergangene_t in self.schritt:
                koor = obj.r.tolist()
                x, y, z = koor
                obj.xs.append(x)
                obj.ys.append(y)
                obj.zs.append(z)

    # speichert die relevanten Daten in einer Json-Datei
    def output(self):
        data = {"Name": self.name, "dt": self.dt, "t": self.t}  # erstellt die relevanten Daten im Json-Format
        for obj in self.objekte[1:]:
            data[f'{obj.obj_id}'] = {'Exzentrizitaet': f'{obj.exzentrizitaet()}', 'Halbachse': f'{obj.semi_a}',
                                     'Umlaufdauer': f'{obj.umlaufperiode(self.objekte[0]) / d}'}
        with open(self.output_file, 'r+') as log: # öffnet die Datei
            content = json.load(log) # lädt den Inhalt der Datei
            content.append(data) # fügt die Daten in den Inhalt ein
            log.seek(0) # geht an den Anfang der Datei
            json.dump(content, separators=(',', ':'), fp=log, indent=len(data)) # fügt Inhalt zur Datei hinzu
            log.truncate() # löscht die alten Daten der Datei

    # speichert die nötigen Koordinaten in .txt datei
    def output_r(self):
        with open(self.output_koords, 'a') as f:
            data = {}
            for obj in self.objekte:
                data[f'{obj.obj_id}'] = {"x": obj.xs, "y": obj.ys, "z": obj.zs}
            json.dump(data, f, indent=len(data))

    # die Simulation des Systems
    def simulation(self):
        self.vergangene_t = 0
        while self.vergangene_t <= self.t:  # die Simulation läuft, bis die Vergangene Zeit nicht mehr kleiner als die Gesamtzeit ist
            self.r_update_rk4()  # berechnet die Position der Objekte
            self.vergangene_t += self.dt

        for obj in self.objekte:
            ax.scatter(obj.xs, obj.ys)

        self.output()
        self.output_r()


# Blueprint für ein Körper
class Objekt:
    def __init__(self, masse=1, a=np.array([0., 0., 0.]), v=np.array([0., 0., 0.]), r=np.array([0., 0., 0.]), obj_id='objekt'):
        self.masse = masse # die Masse des Körpers
        self.a = a # die Beschleunigung des Körpers
        self.v = v # die Geschwindigkeit des Körpers
        self.r = r # die Position des Körpers
        self.semi_a = betrag(self.r) # die Apheldistanz
        self.obj_id = obj_id # zur Identifikation des Körpers

        self.xs = [] # alle x-Koordinaten
        self.ys = [] # alle y-Koordinaten
        self.zs = [] # alle z-Koordinaten
        self.apphel = 0 # die Appheldistanz
        self.perihel = 0 # die Periheldistanz

    # berechnet die Exzentrizität der Umlaufbahn des Körpers
    def exzentrizitaet(self):
        return (self.apphel - self.perihel) / (self.apphel + self.perihel)

    # berechnet die grosse Halbachse
    def semi_ax_up(self):
        self.semi_a = (self.apphel + self.perihel) / 2

    # berechnet die Umlaufperiode des Körpers
    def umlaufperiode(self, obj):
        return 2 * np.pi * np.sqrt(self.semi_a ** 3 / (G * (obj.masse + self.masse)))

