Über Aqserver
=============

Mit diesem Programm können Werte aus einer Simatic S7 Steuerung in eine CSV-Datei aufgezeichnet werden. In Abhängigkeit von der Anzahl der aufzuzeichnenden Werte verändert sich die Zykluszeit der Aufzeichnung, mit steigender Anzahl der Werte steigt auch die Zykluszeit. 

Es können Trigger Bedingungen definiert werden, die eine neue Aufzeichnungsdatei starten. Alte Aufzeichnungsdateien werden komprimiert und in einem definierbaren Verzeichnis abgelegt.
Über Zeiten für Pre- und Posttrigger kann man eine Überlappung von alter und neuer Datei realisieren. Wenn keine Triggerbedingung definiert ist, kann auch von Hand getriggert werden.

In einer Konfigurationsdatei (Standard: aqserver.cfg) werden die Werte für Kommunikation, die aufzuzeichnenden S7 Variablen und noch andere Parameter eingestellt. Öffne die Datei in einem beliebigen Editor und lies die Kommentare, um zu erfahren, wie die Parameter eingestellt werden müssen oder lies das Kapitel "Konfiguration" in diesem Handbuch.

Werte werden in einer CSV-Datei im Unterverzeichnis "data" gespeichert. Der Dateiname kann in der Konfigurationsdatei eingestellt werden. Wenn eine definierte Triggerbedingung erfüllt ist, beginnt eine neue Aufzeichnungsdatei.
Nach einem Trigger oder wenn das Programm beendet wird, wird die Datendatei komprimiert und in einem Verzeichnis gespeichert, welches ebenfalls in der Konfigurationsdatei eingestellt werden kann.
Es ist möglich mehrere Instanzen, mit einer jeweils anderen Konfigurationsdatei, zu starten, um Werte aus unterschiedlichen Steuerungen gleichzeitig aufzuzeichnen.

Bitte beachten, dass sich das Programm noch in der  Entwicklung befindet. Falls es Probleme bei der Benutzung gibt, lies das Kapitel "Probleme" in diesem Handbuch. Dass ein  Problem mit dem Programm in der Steuerung entsteht, ist jedoch nicht zu befürchten.

Für die Visualisierung der aufgezeichneten Daten benutze das Programm Kst2 von https://kst-plot.kde.org. Die Datendatei kann damit online während der Aufzeichnung gelesen und geplottet werden. Dekomprimierte Archive können ebenfalls angezeigt werden. Natürlich können die gespeicherten CSV-Dateien auch mit LibreOffice Calc, MS Excel und anderen ähnlichen Programmen geöffnet und angezeigt werden.