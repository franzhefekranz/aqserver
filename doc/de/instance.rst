Mehrer Instanzen starten
==========================

Wenn von 2 (oder mehr..) Steuerungen gelesen werden soll, müssen mehrere Instanzen von Aqserver gestartet werden:

Erzeuge eine zweite Konfigurationsdatei, die die enstprechenden Parameter für die zweite Verbindung enthalten.

.. note:: Darin muss sich der Name der Datendatei vom Namen in der anderen Instanz unterscheiden!

* benutze einen anderen Namen für die Konfigurationsdatei
* stelle darin einen anderen Namen für die Datendatei ein
* starte Aqserver aus einer Kommandozeile und benutze dazu den -c Parameter
* z.B. unter Windows:

.. code:: text

    >python aqserver.py -c my_new_config_file.cfg

Wenn Aqserver mit dem Windows Setup Programm installiert wurde, kann die Batch Datei im "..\\My Documents\\Aqserver\\" Verzeichnis verwendet werden , um Aqserver zu starten
(siehe dazu das Kapitel "Installation" in diesem Handbuch).
Erstelle eine Batch Datei für jede zu startende Instanz, welche die korrekten Einstellungen für die entsprechende Konfigurationsdatei enthält.
