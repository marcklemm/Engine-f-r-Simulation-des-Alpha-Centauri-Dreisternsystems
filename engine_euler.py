import numpy as np
import json
import matplotlib.pyplot as plt

'''Konstanten'''
G = 6.67430e-11 # Gravitationskonstante
pi = 3.1415926535 # Kreiszahl pi

"""EInheiten"""
yr = 365 * 24 * 3600 # Jahr in Sekunden
d = 24 * 365 # Tag in Sekunden

"""Funktionen"""
def betrag(vek): # berechnet Betrag eines Vektors (Numpy Array)
    return np.sqrt(sum(vek**2))


'''Simulation'''
class System: # System, in welchem sich die Körper bewegen

    def __init__(self, dt, t, name, output_file="log.json"):
        self.objekte = [] # enthält alle Körper, welche sich im System befinden
        self.dt = dt # Zeitintervall
        self.t = t # Gesamtzeit der Simulation
        self.name = name # Name zur Identifikation der Simulation
        self.output_file = output_file # Datei, in welche relevante Informationen über die Simulation gespeichert werden

    def objekt_hinzu(self, *args): # fügt alle Körper, welche für die Simulation verwendet werden sollen zum System hinzu
        for arg in args:
            self.objekte.append(arg)

    def gravitation(self): # berechnet die Beschleunigung der Objekte im System

        for obj in self.objekte: # löscht die Beschleunigung der Objekte
            obj.a = [0, 0, 0]

        for i, obj1 in enumerate(self.objekte):
            for obj2 in self.objekte[i + 1:]:
                richtungs_vek = obj2.r - obj1.r # konstruiert den Vektor zwischen zwei Körpern
                differenz = betrag(richtungs_vek) # bildet die Differenz (Abstand) der Objekte
                f = G * obj2.masse * obj1.masse / differenz ** 3 * richtungs_vek # berechnet die Gravitationskraft als Vektor
                obj1.a += f / obj1.masse # berechnet die Beschleunigung der Objekte aus der Gravitationskraft
                obj2.a += -1 * f /obj2.masse # ""
                if i == 0: # wenn das Objekt der Stern ist, werden alle Abstände der Körper zum Stern berechnet
                    obj2.abstand.append(differenz)

    def r_update(self): # die Position nach dem Zeitintervall dt wird berechnet
        for obj in self.objekte:
            obj.r += obj.v * self.dt + 0.5 * obj.a * self.dt ** 2  # berechnet die Position aller Objekte
            obj.koordinaten.append(obj.r.tolist()) # die Koordinaten werden für die Visualisierung des Systems gespeichert
            obj.v += obj.a * self.dt  # berechnet die Geschwindigkeit der Objekte


    def simulation(self): # die Simulation des Systems

        vergangene_t = 0

        while vergangene_t <= self.t: # die Simulation läuft, bis die Vergangene Zeit nicht mehr kleiner als die Gesamtzeit ist

            self.gravitation()  # berechnet die Beschleunigungen der Objekte
            self.r_update() # berechnet die Position der Objekte

            vergangene_t += self.dt

        """Für die Visualisierung mit matplotlib.pyplot"""
        fig = plt.figure(figsize=(10, 10), tight_layout=True)
        ax = fig.add_subplot(projection='3d')
        for obj in self.objekte:
            obj.r_aufteilen()
            ax.scatter(obj.xs, obj.ys, obj.zs)

        data = {"Name": self.name, "dt": self.dt, "t": self.t} # Erstellt die relevanten Daten im Json-Format
        for obj in self.objekte[1:]:
            data[f'Exzentrizitaet {obj.obj_id}'] = f'{obj.exzentrizitaet()}'
            #data[f'Umlaufperiode {obj.obj_id}'] = f'{obj.umlaufperiode(self.objekte[0])/d}'
        #self.output(data)

    def output(self, data): # Speichert die relevanten Daten in einer Json-Datei
        with open(self.output_file, 'r+') as log: # Öffnet die Datei
            content = json.load(log) # Lädt den Inhalt der Datei
            content.append(data) # Fügt die Daten in den Inhalt ein
            log.seek(0) # Geht an den Anfang der Datei
            json.dump(content, separators=(',', ':'), fp=log, indent=len(data)) # Fügt Inhalt zur Datei hinzu
            log.truncate() # Löscht die alten Daten der Datei


class Objekt: # Erstellt ein Körper
    def __init__(self, masse=1, a=np.array([0., 0., 0.]), v=np.array([0., 0., 0.]), r=np.array([0., 0., 0.]), obj_id='objekt'):
        self.masse = masse # Die Masse des Körpers
        self.a = a # Die Beschleunigung des Körpers
        self.v = v # Die Geschwindigkeit des Körpers
        self.r = r # Die Position des Körpers
        self.obj_id = obj_id # Zur Identifikation des Körpers

        self.koordinaten = [] # Alle Koordinaten wärend der Simulation des Objekts
        self.xs = [] # Alle x-Koordinaten
        self.ys = [] # Alle y-Koordinaten
        self.zs = [] # Alle z-Koordinaten
        self.abstand = [] # Alle Abstände zwischen Körper und Stern

    def r_aufteilen(self): # Teilt die Koordinaten auf
        self.xs = [r[0] for r in self.koordinaten]
        self.ys = [r[1] for r in self.koordinaten]
        self.zs = [r[2] for r in self.koordinaten]

    def exzentrizitaet(self): # Berechnet die Exzentrizität der Umlaufbahn des Körpers
        apphelion = max(self.abstand) # Berechnet den längsten Abstand des Körpers auf der Umlaufbahn um den Stern
        perihelion = min(self.abstand) # Berechnet den kürzesten Abstand des Körpers auf der Umlaufbahn um den Stern
        exzent = (apphelion - perihelion) / (apphelion + perihelion) # berechnet die Exzentrizität
        return exzent

    def umlaufperiode(self, obj): # Berechnet die Umlaufperiode des Körpers
        return 2 * np.pi * np.sqrt(((max(self.abstand) + min(self.abstand)) / 2)**3 / (G * (self.masse + obj.masse)))
