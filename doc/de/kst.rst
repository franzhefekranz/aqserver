Einführung in Kst2
=====================

Kst2 ist ein Open Source Programm, mit dem Daten visualisiert und geplottet werden können. Das Programm kann von  https://kst-plot.kde.org heruntergeladen werden.
Die aktuelle Windows Version ist 2.08.
Auf der Homepage werden einge Tutorial Videos zur Verfügung gestellt. Du solltest vielleicht einen Blick darauf werfen, bevor du das Programm zusammen mit Aqserver benutzt.

Benutzung
---------

.. image:: images/kst/main.png
    :width: 12cm
    :align: center
    :alt: main window

Die einfachste Art Kst zusammen mit Aqserver zu benutzen, ist mit dem "Data Wizard" zu beginnen.

.. note:: Übrigens kann man den Data Wizard auch mehrmals hintereinander starten, wenn man noch Diagramme zur bisherigen Anzeige hinzufügen möchte. Wenn mehrere Instanzen von Aqserver gestartet wurden, können dabei auch die unterschiedlichen Datendateien gewählt werden.


Starte den Data Wizard mit folgendem Icon:

.. image:: images/kst/wizard.png
    :align: center
    :alt: data wizard icon


.. image:: images/kst/wiz1.png
    :width: 12cm
    :align: center
    :alt: data wizard
    
Wenn sich das Data Wizard Fenster öffnet, muss als erstes die aktive Datendatei ausgewählt werden (diese befindet sich in deinem "data" Unterverzeichnis). Wähle die Datei aus und klicke dann auf den "Configure" Knopf.

.. image:: images/kst/wiz2.png
    :width: 12cm
    :align: center
    :alt: configure ASCII file
    
Jetzt öffnet sich das "Configure ASCII file" Fenster. Hier müssen die Eigenschaften der Datendatei eingestellt werden. Folgende Werte müssen (mindestens) eingestellt werden:

* Data starts at line: Scrolle in dem Fenster, das deine Datendatei zeigt, herunter, bis du den ersten Datensatz mit aufgezeichneten Werten erreichst. Merke dir die Zeilennummer und schreibe sie in das entsprechende Feld. Sollte diese Zeile nicht angezeigt werden, hilft dir vielleicht der Knopf "Preview first 1000 lines in new window".
* Offensichtlich muss die "Read field names from:" Option aktiviert werden und die entsprechende Zeilennummer eingetragen werden (obige Zeilennummer - 1)
* stelle das Dezimaltrennzeichen ein
* stelle das Wertetrennzeichen so ein wie in der Datendatei.
* Aktiviere "Date/Time Interpretation"
* Scrolle die Dropbox "Interpret field as" herunter und wähle den Wert "timestamp". Wenn keine Auswahl angeboten wird, verlasse das Fenster mit "ok" und öffne es dann erneut. Jetzt sollte eine Auswahl vorhanden sein. Wähle "timestamp".
* aktiviere  "formatted string" und stelle das Format auf  "yyyy-MM-dd hh:mm:ss.zzz" ein. Dann wird unser Zeitstempel korrekt interpretiert.

Verlasse das Fenster jetzt mit "Ok". Setze den Update Typ auf entweder "time interval" oder du kannst auch "change detection" ausprobieren.
Wenn nur eine dekomprimierte Archivdatei angezeigt werden soll, kann "no update" verwendet werden. Klicke dann auf "Next" im Data Wizard.

.. image:: images/kst/wiz3.png
    :width: 12cm
    :align: center
    :alt: Preview first 1000 lines in new window
    
Data wizard mit  "Preview first 1000 lines in new window".

.. image:: images/kst/wiz4.png
    :width: 12cm
    :align: center
    :alt: pick values to diplay
    
Wähle die Werte, die in einem Diagramm angezeigt werden sollen und bringe sie auf die rechte Seite mit den Pfeiltasten. Klicke dann auf "Next".

.. image:: images/kst/wiz5.png
    :width: 12cm
    :align: center
    :alt: pick values to diplay with values selected
    
Das Gleiche mit einigen ausgewählten Werten.

.. image:: images/kst/wiz6.png
    :width: 12cm
    :align: center
    :alt: plot settings
    
Experimentiere mit den Datenbereichseinstellungen. Aktiviere "Create XY-plots". Für den X-Achsen Vektor wählen wir unser Feld "timestamp". Klicke dann auf "Next".

.. image:: images/kst/wiz7.png
    :width: 12cm
    :align: center
    :alt: layout settings
    
Stelle die Anzeige der Diagramme je nach Wunsch auf "in one plot" oder "1 plot per curve".



.. image:: images/kst/offline.png
    :width: 15cm
    :align: center
    :alt: result
    
Jetzt sollten die aufgezeichneten Werte angezeigt werden. Falls du eine aktuelle Datendatei gewählt hast, sollten sich die Diagramme auch aktualisieren.

.. note:: Wenn ein Trigger für eine neue Datendatei ausgelöst wurde, benutze den Knopf mit dem grünen runden Pfeil, um die Datei zu aktualisieren. 
    Sonst wird bei einem Wechsel auf eine neue Datei nichts mehr angezeigt.

Für detaillierte Information über Kst2, lies die Dokumentation oder browse durch die Foren usw.

Hinzufügen einer Anzeige des aktuellen Werts
--------------------------------------------

Soll im Diagramm der aktuelle Wert angezeigt werden, kann man dies mit dem Textwerkzeug realisieren.
Dazu gehe wie folgt vor:

* Aktiviere das "Label" Werkzeug, es öffnet sich ein Fester zur Eingabe des Textes

.. image:: images/kst/label.png
    :width: 2cm
    :align: center
    :alt: Label-Werkzeug

.. image:: images/kst/label1.png
    :width: 12cm
    :align: center
    :alt: Eingabefenster
    
* Gib deinen Text ein. Um den aktuellen Wert einzufügen, klicke rechts und wähle
 "Insert new scalar". Es öffnet sich das Fenster zur Einstellung für den neuen Skalar.

.. image:: images/kst/label2.png
    :width: 12cm
    :align: center
    :alt: Fenster für neuen Skalar
    
* Hier stellen wir folgendes ein:

     * aktiviere "Read from data vector"
     * wähle den gewünschten Wert aus der Dropdownliste
     * aktiviere das Kästchen "last frame" und akzeptiere die Einstellungen mit Ok
* Zurück im Eingabefenster für das Label, kann noch das Format des Wertes hinzugefügt werden
 (Näheres steht in der Hilfe, Button "Help")
 Nach Fertigstellung verlasse die Eingabe mit "Ok"

.. image:: images/kst/label3.png
    :width: 12cm
    :align: center
    :alt: Fenster mit dem fertigen Label

* Platziere jetzt das Label mit der Maus, bei Klick wird das Label platziert.

.. image:: images/kst/label4.png
    :width: 12cm
    :align: center
    :alt: Diagramm mit Label
    
.. image:: images/kst/label5.png
    :width: 6cm
    :align: center
    :alt: Label

Das Label sollte sich jetzt aktualisieren und den aktuellen Wert anzeigen.