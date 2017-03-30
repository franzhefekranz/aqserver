Benutzung des Programms
=======================

Starten aus einem Python Terminal
---------------------------------

In einem Python Terminal kann das Programm wie folgt gestartet werden:

.. code:: text

    >python aqserver.py

oder

.. code:: text

    >aqserver.py

Wird das Programm ohne angehängte Parameter gestartet, wird der Standardname für die Konfigurationsdatei "aqserver.cfg" verwendet.

Es ist eine gute Idee, für jede Installation, an der aufgezeichnet werden soll, eine separate Konfigurationsdatei zu erstellen. In diesem Fall, wenn nicht die Standard-Konfigurationsdatei verwendet wird, wird so gestartet:

.. code:: text

    >aqserver.py -c my3rd.cfg

oder eben wie der Name der verwendeten Konfigurationsdatei ist. Es ist empfehlenswert die Erweiterung ".cfg" für die Konfigurationsdatei zu benutzen. Prinzipiell funktioniert es auch ohne die Erweiterung, benutze immer den kompletten Namen, inklusive der Erweiterung.


.. image:: images/usage1.png
    :align: center
    :alt: Console showing Aqserver in run

Wie man dem obigen Bild entnehmen kann, zeigt das Programm ein paar Optionen sowie die Anzahl der Datensätze in der aktuellen Datendatei und die Anzahl der bis jetzt aufgezeichneten Archivdateien an.
Die Optionen sind:

* ESC - Programm beenden : Mit Drücken der "ESC" Taste wird die aktuelle Datendatei gespeichert und das Programm wird beendet.
* P - Pause: die Aufzeichnung kann mit der Taste "P" unterbrochen werden. D.h. es wird nicht von der Steuerung gelesen und auch nichts  in die Datendatei geschrieben. Dies kann nützlich sein, wenn z.B. die Produktion einer Maschine gestoppt wurde, die aktuelle Datendatei jedoch weiter verwendet werden soll.
* S - Start: Wenn die Aufzeichnung mit "P" unterbrochen wurde oder die Einstellung "autostart" auf 0 steht, dann kann die Aufzeichnung mit der Taste "S" gestartet / fortgesetzt werden.
* T - Neue Datei triggern: Mit der Taste "T" kann ein Trigger für eine neue Datendatei von Hand ausgelöst werden.  Die aktuelle Datendatei wird archiviert und eine neue Datendatei wird gestartet. Dies wird mit der Anzahl der aufgezeichneten Dateien angezeigt, außerdem startet die Anzahl der Datensätze wieder bei 1.

.. note:: Für die Tasten muss natürlich nicht auf Groß- oder Kleinschreibung geachtet werden.

Benutzung der Windows Installer Version
---------------------------------------

Wenn Aqserver mit dem Windows Setup Programm installiert wurde, dann ist die Benutzung etwas anders als oben beschrieben. Es kann auch sein, dass keine Python Umgebung installiert ist.
Das Setup Programm installiert die Aqserver.exe nach "C:\\Program Files (x86)\\Aqserver\\". Eine Beispielkonfiguration und eine Batch Datei wird nach "..\\My Documents\\Aqserver\\" kopiert. 
Wenn die Konfigurationsdatei bearbeitet und fertiggestellt wurde, sollte eine Kopie der Batch Datei bearbeitet werden, so dass Aqserver mit deiner eigenen Konfigurationsdatei gestartet wird.
Inhalt der Batch Datei:

.. code:: text

    "C:\Program Files (x86)\Aqserver\aqserver.exe" -c "path_to\test.cfg"
    pause


Passe Pfad und Name deiner Konfigurationsdatei an. Danach kann Aqserver mit einem Doppelklick auf die Batch Datei aus dem Windows Explorer gestartet werden.

