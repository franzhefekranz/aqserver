Neu in dieser Version
=====================
V0.3
15 Oktober 2020

* aqserver.py: Erweiterung der config-Datei: bei der Eingabe der Werte muss jetzt eine Verstärkung, eine Verschiebung und die Einheit angegeben werden. Die Einheit im Namen entfällt.
* aqserver.py: Der Header wird von den Daten getrennt, Die Datendatei wird bei jedem Trigger (Hand/Konfiguriert/max. Anzahl Werte) gespeichert. Der Header wird mit Zeitstempel nur bei Beenden des Programms im Archivverzeichnis gespeichert. Dies hat den Vorteil, dass bei Änderungen der Anzahl Werte in der config-Datei eine bestehende kst-Datei weiter funktioniert, allerdings nur wenn die bestehenden Wert unverändert bleiben. Also nur neue Wert an die Liste anhängen, nur dann wird die Reihenfolge nicht geändert.
* aqserver.py: In der Anzeige der Konsole einen Fortschrittsbalken eingefügt
* Dokumentation aktualisiert und erweitert
* Installationsdatei umbenannt: Aqserver-x.x.x.exe dabei ist x.x.x die Programmversion, z.B. Aqserver-0.3.exe
* die Demo config-Datei aktualisiert, mit Dokumentation für Verstärkung/Verschiebung/Einheit


Für eine komplette Änderungshistorie siehe Changelog!