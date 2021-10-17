import bpy
from pathlib import Path
import json

"""Optionen"""
skalierung = 10 ** 13
frame_schritt = 5
dateipfad = 'C:/Users/...'

# Array aller Objekte im System
objects_arr = []


# definiert Objekt
class Object:
    def __init__(self, xs=[], ys=[], zs=[]):
        # die Koordinaten
        self.xs = xs
        self.ys = ys
        self.zs = zs
        # erstellt einen Ball in Blender für die Visualisierung
        bpy.ops.object.metaball_add()
        # fügt das Objekt der Array hinzu
        objects_arr.append(self)

    # konvertiert den Dateipfad


path = Path(bpy.path.abspath(dateipfad))
# ruft den definierten Dateipfad ab
with open(path, 'r') as f:
    content = json.load(f)
    # erstellt ein Objekt für jeden Eintrag in der Datei und fügt die Angegebenen Koordinaten dem Objekt hinzu
    for key, values in content.items():
        Object(xs=content[key]['x'], ys=content[key]['y'], zs=content[key]['z'])

# erstellt für jede Koordinate ein Keyframe und ändert die Position der Objekte
for i, object in enumerate(objects_arr):
    frame_number = 0
    # ruft das Objekt am index i ab
    obj = bpy.data.objects[i]
    # wählt das genannte Objekt aus, welches modifiziert werden soll
    obj.select_set(True)
    # setzt die Position des Objektes für jedes Keyframe
    for j in range(len(object.xs)):
        # ruft das Keyframe ab
        bpy.context.scene.frame_set(frame_number)
        # ändert die Position des Objektes und verkleinert die Werte
        x = object.xs[j] / skalierung
        y = object.ys[j] / skalierung
        z = object.zs[j] / skalierung
        obj.location = [x, y, z]
        # erstellt ein Keyframe
        obj.keyframe_insert(data_path="location", index=-1)
        frame_number += frame_schritt
    # entwählt das Objekt
    obj.select_set(False)
