Probleme
===========

Wenn sich das Programm unerwartet beendet oder abstürzt, dann sollte das Debugging eingeschaltet werden. Standardmäßig ist das Debugging ausgeschaltet.
Um das Programm mit eingeschaltetem Debugging zu starten, öffne die Konfigurationsdatei und setze den Parameter "dbglevel" auf einen Wert > 0 (siehe unten). Der Wert 1 für INFO ist dabei die redseligste Einstellung.
Bei Problemen sollte mindestens auf 3 eingestellt werden.

.. code:: text

	###############################################################################
	# debug settings
	###############################################################################
	[debug]

	# debug level
	# set logging level to debug, write program actions
	# to logfile
	# 0 - no logging
	# 1 - log INFO messages (default setting)
	# 2 - log WARNING messages
	# 3 - log DEBUG messages
	# 4 - log ERROR messages
	# 5 - log CRITICAL messages
	# 6 - log EXCEPTION messages
	dbglevel = 0 

    
Das Programm sollte danach noch einmal gestartet werden. Nach Beendigung muss die Log-Datei im Unterverzeichnis "log" geprüft werden.
Darin sollten detailliertere Angaben, warum das Programm nicht ordnungsgemäß funktioniert, zu finden sein.
Korrigiere (vermutlich) deine Konfiguration entsprechend und versuche es erneut.

Probleme können verursacht werden durch:

* die Steuerung kann mit den eingestellten Parametern nicht erreicht werden
* Werte in deiner Liste sind in der Steuerung nicht vorhanden
* Schreibfehler in den Konfigurationswerten

Wenn all dies nicht zum Erfolg führt, schicke eine Kopie deiner Log- und der Konfigurationsdatei an meine Mailadresse (aqserver at taxis-instruments dot de). 

Häugig gestellte Fragen FAQ:
----------------------------

Keine bis jetzt. Dieser Abschnitt wird aktualisiert, sobald sich Fragen ergeben. Fragen können im Kontaktformular unter http://taxis-instruments.de/sample-page/kontakt gestellt werden oder schicke eine Email an <aqserver at taxis-instruments dot de>