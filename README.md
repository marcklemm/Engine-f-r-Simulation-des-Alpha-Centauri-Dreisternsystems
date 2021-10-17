# Engine für Simulation von gravitativ-interagierende Körper
Das Engine dient der Simulation von gravitativ-interagierenden Körpern (N-Körpersysteme). Die verwendeten Integrationsverfahren sind einerseits die Euler-Methode, welche allerdings weniger effizient ist und eine geringere Genauigkeit aufweist, und anderseits das Runge-Kutta-Verfahren 4. Ordnung, welches nicht nur genauer, sondern auch stärker optimiert wurde, ist.

main.py ist für die Konfiguration der Simulation zuständig. Hier können alle relevanten Anfangsbedingungen angegeben werden. Körper können mit der class Object() erstellt und einem System, welches mit der class System() zu erstellen ist, mit objekt_hinzu() hinzugefügt werden. Die Simulation wird dann mit der method simulation() initialisiert.
engine_rk4.py enthält die Engine der Simulation, welche auf RK4 basiert.
engine_euler.py enthält die Engine der Simulation, welche auf dem Euler-Verfahren basiert.
log.json speichert die Orbitalparameter der Körper ab.
koordinaten.txt speichert die Koordinaten der Körper für die Visualisierung ab. Wichtig ist, dass die Koordinaten nach jeder Simulation geleert werden, da visual.py nur ein System auslesen und visualisieren kann.
visual.py beinhaltet das Skript für die Visualiserung mit Blender. Die Koordinaten werden aus koordinaten.txt bezogen.


