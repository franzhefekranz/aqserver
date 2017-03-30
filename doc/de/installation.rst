Installation
============
Das Programm kann unter https://github.com/franzhefekranz/aqserver heruntergeladen werden.

Das Programm wurde mit Python 2.7.10 unter Windows 7 - 32 bit geschrieben.

Installation mit dem Quellcode
______________________________

Wenn direkt mit dem Quellcode gestartet werden soll, muss eine lauffähige Python Umgebung installiert sein. Empfehlenswert dafür sind für ein Windows Betriebssystem z.B. die Python (x,y) Distribution von https://python-xy.github.io/ oder Winpython von https://winpython.github.io/ .  Unter Linux oder MacOS sollte Python bereits als Teil des Betriebssystems installiert sein.

Im Programm werden folgende Bibliotheken zumindest teilweise verwendet (nicht in bestimmter Reihenfolge):

* time
* sys
* os
* shutil
* ctypes
* struct
* logging
* collections
* win32com
* python-snap7
* socket
* datetime
* gzip
* bz2
* binascii
* ConfigParser
* distutils

Diese Bibliotheken können, wenn nicht bereits vorhanden, mit pip installiert werden.

Python-snap7 ist ein Python Wrapper für die snap7 Bibliothek von http://snap7.sourceforge.net/ . Bitte sicherstellen, dass auch diese Bibliothek installiert ist.

Installieren mit dem Windows Setup
__________________________________


Für die Installation kann auch das im Repository im Unterverzeichnis nsi verfügbare Installationsprogramm verwendet werden. Starte das setup.exe als Administrator und folge dem Anweisungen des Programms.
Eine Verknüpfung zum Programm wird im Startmenü installiert. Das Programm selbst wird im Verzeichnis "C:\\Program Files (x86)\\Aqserver\\" installiert.
Zusätzlich wird das Verzeichnis "Aqserver" mit den Unterverzeichnissen "help", "log" und "data" im Verzeichnis "Eigene Dokumente" des aktuellen Benutzers angelegt.
Im "Aqserver" Verzeichnis findest du folgende Dateien:

* test.bat: eine Windows Command/Batch Datei, welche Aqserver mit einer Testkonfiguration startet. Diese Datei kann kopiert und bearbeitet werden, um sie an die entsprechenden Anforderungen anzupassen. Ich benutze diese Datei, um Aqserver aus dem Windows Explorer zu starten oder um mehrere Instanzen des Programms zu starten (eine Batch Datei pro Instanz).
* test.cfg: ein Beispiel für eine Konfigurationsdatei, die an die persönlichen Anforderungen angepasst werden muss. (Es ist eine gute Idee, vorher eine Kopie der Datei zu erstellen..)

 
Um Aqserver zu deinstallieren, starte den Uninstaller aus dem Startmenü oder deinstalliere aus der Systemsteuerung.

Händische Installation
_______________________

Um Aqserver auf einem Windows Betriebssystem ohne Python Umgebung zu installieren, benutze ein Verzeichnis deiner Wahl und kopiere die Dateien aqserver.exe, aqserver.cfg, aqserver.chm and aqserver.pdf in dieses Verzeichnis. Kopiere "snap7.dll" in dein "Windows\\system32 " Verzeichnis.
Lösche diese Dateien, um zu deinstallieren.
