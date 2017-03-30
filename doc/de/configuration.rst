Konfigurationsdatei für Aqserver
================================

Zum Starten des Programms  wird eine Konfigurationsdatei benötigt, in der alle notwendigen Parameter zur Aufzeichnung hinterlegt sind. Beim Start wird die Konfigurationsdatei eingelesen, die Parameter auf Korrektheit überprüft und danach die Aufzeichnung gestartet.

Regeln in der Konfigurationsdatei
---------------------------------

Einstellungen über mehrere Zeilen müssen mit TAB eingerückt werden, siehe unten Beispiel "remarks".

In der Konfigurationsdatei starten Kommentare mit "#":

"#" in der ersten Spalte definieren die Zeile als Kommentar, dies kann auch zum Auskommentieren von Einstellungen benutzt werden. Es muss jedoch immer eine gültige Einstellung vorhanden sein.

Benutze ";" um nach einer Einstellung in derselben Zeile einen Kommentar einzufügen

Einstellungen in der Konfigurationsdatei
----------------------------------------

Aqdata Einstellungen
~~~~~~~~~~~~~~~~~~~~

Zur Information können verschiedene Texte in der Konfigurationsdatei hinterlegt werden, diese werden im Kopf der Datendatei eingefügt.
Es kann ein Feldname ab der ersten Spalte gefolgt von "=" und dem gewünschten Text, hinzugefügt werden.

.. note:: Alle Einstellungen werden in der Datendatei eingefügt. Wird ein entpacktes Archiv im Editor geöffnet, können die Einstellungen herauskopiert werden, um eine neue Konfigurationsdatei zu erstellen, falls die Originaldatei verloren gegangen ist.

.. code:: text

    ########################################################################
    # aqdata settings
    ########################################################################
    [aqdata]
    place = somewhere

    creator = Michael Taxis

    machine = MyMachine

    order = 123456
    
    yourText = type whatever you desire

    remarks = ; use tab for multiline values
        trials with double spreader, to get rid of married rolls
        trials for SF production


Einstellungen für die Kommunikation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Zur Kommunikation mit der S7 werden folgende Parameter benötigt:

* demo: Aqserver kann in Demomodus laufen die Werte werden zufällig erzeugt, ohne Kommunikation mit einer Steuerung
* IP address: IP Addresse der Steuerung die erreicht werden soll. Bestätige mit einem PING vor dem Start!
* rack number: ist normalerweise immer 0
* slot number: das ist normalerweise die Nummer links neben der CPU in der Hardware Konfiguration, im Bild unten die 3.
* maximum connection attempts: Das Programm versucht sich mit der Steuerung zu verbinden. Falls nach dieser Anzahl Verbindungsversuche keine Verbindung zustande kommt, wird das Programm beendet. Prüfe dann die Konfiguration und deine Verbindung (Kabel, PING, evtl. Firewall...). Wird dieser Wert auf 0 gestellt, wird in einer Endlosschleife versucht die Verbindung aufzubauen und das Programm bricht nicht ab. Dies kann hilfreich sein, wenn das Programm  unbeobachtet z.B. über Nacht aufzeichnen soll. Sollte in diesem Fall keine Verbindung zustande kommen, kann das Programm mit CTRL + C bzw. STRG + C abgebrochen werden. Wird die Kommunikation während der Aufzeichnung unterbrochen, versucht das Programm die Verbindung wieder aufzubauen. Es können aber natürlich keine Werte aufgezeichnet werden, wenn die Verbindung unterbrochen ist.

.. image:: images/hwconfig.png
    :align: center
    :alt: HW config

.. code:: text

    ########################################################################
    # communication settings
    ########################################################################
    [communication]

    # setting up communication parameters to S7-PLC
    # ATTENTION: config values are case sensitive
    # ip, rack and slot must be in lowercase letters!
    
    # demo switch
    # if 1 communication will be ignored and values will be randomly created
    # if 0 then aqserver tries to connect to a plc
    demo = 0

    # IP address
    # you can leave several settings , just comment with a leading "#"
    #ip = 192.168.1.107
    ip = 172.16.13.174

    # rack number, see HW Config
    rack = 0

    # slot number of CPU, see HW Config
    slot = 3

    # maximum attempts for connection, 0 is trying forever
    maxattempts = 10
    
.. note:: Aqserver kann auch mit PLCSIM und NetToPlcsim von http://nettoplcsim.sourceforge.net/ getestet werden.

Verschiedene Einstellungen
~~~~~~~~~~~~~~~~~~~~~~~~~~

Wir brauchen ein paar grundsätzliche Einstellungen für Aqserver:

* delimiter: Dies ist das Trennzeichen, das die Werte in der Datendatei voneinander trennt, falls nichts anders dagegen spricht benutze ";". Bitte nicht das Dezimaltrennzeichen des Betriebssystems verwenden (also  "." oder "," NICHT verwenden)!
* datafileprefix: Es kann ein Name definiert werden, der im Namen der Archivdatei verwendet wird. Dies ist ein Namensvorsatz, da der Dateiname auch noch einen Zeitstempel enthält, z.B.: MyProject20150804_173035.csv.gz
* datafile ist der Dateiname (ohne Erweiterung) der Datendatei für die aktuelle Aufzeichnung. Die Datei ist eine CSV-Datei. Falls mehrere Instanzen für unterschiedliche Steuerungen aufgezeichnet werden sollen, muss für jede Instanz eine anderer Dateiname in den separaten Konfigurationsdateien verwendet werden!
* autostart: definiert ob die Aufzeichnung direkt mit Programmstart anläuft oder ob auf ein manuelles Startsignal (Taste "S") gewartet wird.
* datapath: hier stellen wir ein, wo die Archive abgelegt werden.
* usedir: definiert ob wir eine Verzeichnisstruktur (\\JJJJ\\MM\\TT\\)zur Ablage der Archive verwenden.
* scantime: Zykluszeit in [ms], minimale Zykluszeit ist auf 20 ms im Programm begrenzt. Die Zeit ist nur eine ungefähre Angabe und ist auch von der Anzahl der zu lesenden Variablen abhängig. Der Wert kann verwendet werden um die Dateigröße zu reduzieren. Je kleiner der Wert umso größer wird die Datei. Wird der Wert auf "0" gesetzt, werden die Daten so schnell wie möglich gelesen (Vorsicht: große Datei!). Je nach Anzahl der Variablen können Zykluszeiten bis ~10 ms erreicht werden. 
* maxrecords: Diese Zahl definiert die maximale Anzahl der Aufzeichnungen in einer Datei. Damit kann die Größe der Datei begrenzt werden. In Abhängigkeit von der Anzahl der Variablen sollte geprüft werden, welcher Wert hier anwendbar ist.
* booloffset: wenn dieserWert auf 1 gesetzt wird, wird zu den Bits in einem Byte ein Offset addiert, wie folgt:
    Wert + Bit Nummer * 2
     
    Dadurch können die Bits in Kst in einem Plot angezeigt werden ohne zu überlappen

    .. table::

        +------+------+-------+
        |  bit | true | false |
        +======+======+=======+
        |  0   |  1   | 0     |
        +------+------+-------+
        |   1  |  3   |  2    |
        +------+------+-------+
        |   2  |  5   |  4    |
        +------+------+-------+
        |   3  |  7   |  6    |
        +------+------+-------+
        |   4  |  9   |  8    |
        +------+------+-------+
        |   5  | 11   | 10    |
        +------+------+-------+
        |   6  | 13   | 12    |
        +------+------+-------+
        |   7  | 15   | 14    |
        +------+------+-------+

    Ist der Wert 0 wird nur der boole'sche Wert gespeichert (1 für true, 0 für false). 


.. code:: text

    ########################################################################
    # miscellaneous settings
    ########################################################################
    [misc]

    # miscellaneous values for setting up the acquisition server
    # value delimiter in storage file
    delimiter = ;

    # prefix of data file name, e.g. a customer/project name or whatever
    datafileprefix = MyProject

    # data file name for actual data recording, without extension!
    # e.g. if you use "filename", actual name will be "filename.csv"
    datafile = recording

    # autostart: when program is started decide whether acquisition is started(1)
    # immediately or wait for start signal (0)
    autostart = 0

    # path for data files, use "\" for directory separation, with "\" at the end !
    # e.g. datapath = D:\mydata\
    datapath = F:\aqdata\MyProject\

    # if 1 use directory structure datapath\yyyyy\MM\dd otherwise use only datapath
    usedir = 1

    # scantime in milliseconds [ms]
    # if you just put 0 program will scan as fast as possible
    # this will produce rather large data files!
    # depending on number of values this value is just a hint ;-)
    scantime = 100
    
    # maximum number of records
    # to avoid too big data files, a new one will be started after this number
    # of recordings
    maxrecords = 50000

    # switch for offset of boolean values
    # if 1 then boolean values in a byte (see values settings) will be offset by 2 as follows:
    #
    # value + bit number * 2
    #
    #  bit | true | false
    #  ----+------+-------
    #   0  |  1   +  0
    #  ----+------+-------
    #   1  |  3   +  2
    #  ----+------+-------
    #   2  |  5   +  4
    #  ----+------+-------
    #   3  |  7   +  6
    #  ----+------+-------
    #   4  |  9   +  8
    #  ----+------+-------
    #   5  | 11   + 10
    #  ----+------+-------
    #   6  | 13   + 12
    #  ----+------+-------
    #   7  | 15   + 14
    # if booloffset is 0 then only the boolean value (1 for true, 0 for false) will be stored
    booloffset = 1

Trigger Einstellungen
~~~~~~~~~~~~~~~~~~~~~

Die Trigger Einstellungen werden benutzt, um die Bedingung für den Start einer neuen Datendatei zu definieren. Ein Trigger kann auch per Hand (Taste "T") ausgelöst werden. 
Eine Triggerbedingung wird durch die folgenden 3 Einstellungen definiert:

* trgsignal: dies ist der Name des Signals aus den Werteeinstellungen (s.u.), auf welches getriggert werden soll. Kopiere den Namen aus den Werteeinstellungen.
* trgcondition: dies ist die Vergleichsbedingung für das Triggersignal mit dem Triggerwert. Wenn z.B. die Bedingung  "==" ist, dann wird getriggert wenn das Signal gleich dem Wert ist.
* trgvalue: dies ist ein Wert bzw. eine Konstante mit dem das Triggersignal verglichen wird, um den Trigger auszulösen.

Desweiteren werden 2 Einstellungen benötigt, wenn alte und neue Datendatei sich überlappen sollen:

* pretrg: Zeit in [s] die in der neuen Datei VOR dem Trigger aufgezeichnet wird. Basiert auf der Einstellung scantime, pretrg geteilt durch scantime ergibt die Anzahl der Datensätze.
* posttrg: Zeit in [s] die in der alten Datei NACH dem Trigger aufgezeichnet wird. Basiert auf der Einstellung scantime, posttrg geteilt durch scantime ergibt die Anzahl der Datensätze.

.. code:: text

    ########################################################################
    # trigger settings
    ########################################################################
    # when trigger condition is matched, then we close the old file after 
    # post-trigger time and start the new file and copy pre-trigger time 
    # and post-trigger recordings to new file
    #    # condition is, with example:
    # trgsignal trgcondition trgvalue
    # rewind diameter [mm] = 0
    #
    [trigger]

    # trigger signal, copy the name of the signal in [values] section,
    # that you want to use as trigger signal
    trgsignal = rewind diameter [mm]

    # trigger condition, use >,>=,==, <=,<,!= as condition
    # when conditon is matched, then we close the old file and start a new one
    # trgcondition = >
    # trgcondition = >=
    # trgcondition = ==
    trgcondition = <=
    # trgcondition = <
    # trgcondition = !=

    # trigger value, with this value we compare the trigger signal
    trgvalue = 0

    # pre-trigger time in seconds [s]
    # will still add pre-trigger/scantime lines to old file after trigger event
    # e.g. pre-trigger is 60 seconds and scantime is 100 ms, then 600 lines 
    # will be recorded after trigger event
    pretrg = 30

    #post-trigger time in seconds [s]
    # will copy last post-trigger/scantime lines from old to new file
    # e.g. post-trigger is 60 seconds and scantime is 100 ms, then 600 lines will
    # be copied after trigger event
    posttrg = 30

Debug Einstellungen
~~~~~~~~~~~~~~~~~~~

Die Debug Einstellungen definieren wie und ob der Prorgammablauf zur Fehlersuche geloggt wird.

Dazu müssen wir einen Debug Level einstellen, der festlegt, was geloggt wird.

Mit dem Wert "0" wird das Logging deaktiviert, mit Level "1" wird alles geloggt.
Bitte beachten, dass bei jedem Neustart des Programms, das Verzeichnis mit den Log-Dateien geleert wird, so dass nur die jeweils neueste Log-Datei erhalten bleibt.

Der Parameter logfile definiert den Namen der Log-Datei, ohne Erweiterung. Erweiterung ist immer ".log".

Wird der Parameter logts auf 1 gesetzt, wird jedesmal, wennn das Programm gestartet wird, eine neue Log-Datei angelegt. Ist logts = 0, dann wird an eine bestehende Log-datei angehängt.

.. code:: text

    ########################################################################
    # debug settings
    ########################################################################
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
    dbglevel = 2

    # name of logfile, without extension. Extension will be added as ".log"
    logfile = aqserver

    # add timestamp to logfile name 1 = yes, 0 = no
    # if set to 1 a timestamp will be added to the lofile name. pls. note that a
    # new logfile will be created, every time you start the server,
    # when dbglevel is > 0
    logts = 1



Werteeinstellungen
~~~~~~~~~~~~~~~~~~



In den Werteeinstellungen listen wir die Werte bzw. Steuerungsvariablen auf, die aufgezeichnet werden sollen.
Eine Wertedifinition besteht aus einem Wertenamen gefolgt von einem Gleichheitszeichen und der Adresse der Variablen, die gelesen werden soll.
Im Namen kann innerhalb von eckigen Klammern [] die Einheit des Wertes angegeben werden. Die Einheit wird aus dem Namen extrahiert und in eine extra Zeile in der Datendatei geschrieben.

Die Definition der Adresse folgt allerdings nicht der S7 Syntax, da unsere Syntax die Adresse, das Format (bool, int, float) und die Größe der Variablen in bytes (bool, byte, word, double word) in einem Parameter enthält. Dies ist bei der S7 Syntax nicht eindeutig, da z.B. ein Doppelwort sowohl das Format DINT als auch REAL haben kann. Die Syntax ist im Detail unten beschrieben.

Die Definition von booleschen Variablen ist etwas speziell, da die kleinste Größe die gelesen werden kann, ein Byte ist. Deshalb wird ein byte in 8 einzelne boolesche Variablen aufgesplittet.
Um festzulegen welches bool von diesen 8 aufgezeichnet werden soll, müssen die Namen der einzelnen booleschen Variablen mmit einem "," getrennt werden (in einer Zeile). Wird dann der Text zwischen 2 Kommas weggelassen, wird diese Variable zwar gelesen, jedoch nicht in die Datendatei geschrieben.

Zum besseren Verständnis folgend eine Tabelle, wo wir die S7 Syntax mit unserer Syntax vergleichen:

.. table::

    +-------------------------+-------------------------+-------------------------+
    | S7 Syntax               | Format                  |  Aqserver syntax        |
    +=========================+=========================+=========================+
    | DB4615.DBD714           | REAL                    | DB4615.DF714            |
    +-------------------------+-------------------------+-------------------------+
    | ED 4                    | DINT                    | ED4                     |
    +-------------------------+-------------------------+-------------------------+
    | DB4615.DBD714           | DINT                    | DB4615.DD14             |
    +-------------------------+-------------------------+-------------------------+
    | AW 4                    | INT                     | AW 4                    |
    +-------------------------+-------------------------+-------------------------+
    | DB4615.DBB6             | INT                     | DB4615.DB6              |
    +-------------------------+-------------------------+-------------------------+
    | DB4615.DBX6.1           | BOOL                    | DB4615.DX6 (byte!)      |
    +-------------------------+-------------------------+-------------------------+


    

.. code:: text

    ########################################################################
    # value settings
    ########################################################################
    # here we define the S7 variables we want to read, and their formats
    # here we define the S7 variables that we want to observe
    # use following syntax:
    #
    ######### how to define the names: ########################################
    # use config value name with [ ] - brackets to define the unit of the value
    # units will be separated from the name and put into the datafile
    #
    # boolean values:
    # For boolean values (see format X above) a complete byte is read and then
    # split into 8 bits
    # To define names for the single bits use ',' to separate the names, e.g.:
    #
    # bit0,bit1,bit2,bit3,bit4,bit5,bit6,bit7 = DB1234.DX5
    # Ventil 1, Ventil 2, Ventil 3, Ventil 4, Res1, Res2, Res3, Res4 = DB1234.DX5
    #
    # If you do not want all the bits, leave the name empty e.g.:
    #
    # bit0,,bit2,,,,, = DB1234.DX5
    #
    # This reads only bit0 and bit2
    #
    #
    ######### how to define the values: ############################################
    # (S7 variable and format)
    # DBn.AFn.x
    #
    # where:
    # - DB is for data blocks or omitted if other area
    # - n is DB number or omitted if other area
    #
    # - . only when data, omitted otherwise
    #
    # - A is area
    #   - D for data
    #   - M or F for flags
    #   - E or I for inputs
    #   - A or Q for outputs
    #   - T for timers
    #   - Z or C for counters
    #
    # - F is format:
    #
    #   - X - for BYTE in BOOL format, followed by byte address:
    #   - n is whole number for byte address
    #     (attention to address ranges of PLC)
    #     will always be split in 8 single booleans
    #
    #   - B - for BYTE in int format, followed by byte address
    #   - n is whole number for byte address
    #   (attention to address ranges of PLC)
    #
    #   - W - for WORD, followed by byte address
    #   - n is whole number for byte address
    #   (attention to address ranges of PLC)
    #
    #   - D - for DOUBLE WORD, followed by byte address
    #   - n is whole number for byte address
    #   (attention to address ranges of PLC)
    #
    #   - F - for DOUBLE WORD in REAL format, followed by byte address
    #   - n is whole number for byte address
    #   (attention to address ranges of PLC)
    #
    #
    [values]
    rewind diameter [mm] = DB4615.DF714
    webspeed actual [m/min] = DB4615.DF574
    vibration left core chuck [mm/s] = DB4614.DF560
    vibration right core chuck [mm/s] = DB4614.DF564
    vibration rider roll [mm/s] = DB4614.DF568
    #Klemmventil UM1,Klemmventil UM2,Klemmventil UM3,Klemmventil UM4,,,, = DB4614.DX564
