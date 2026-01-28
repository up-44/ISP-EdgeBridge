# 🛠 Troubleshooting & Problemlösungen


## 💾 Datenbank (PostgreSQL)

1. Fehler: duplicate key value violates unique constraint "sensor_readings_pkey"
Problem: Versuch, einen Datensatz mit einer ID einzufügen, die bereits existiert.

Ursache: Manuelle ID-Vergabe im n8n-Workflow oder Konflikte beim Testen.

Lösung: Umstellung der Primärschlüssel-Spalte auf GENERATED ALWAYS AS IDENTITY. Die Datenbank übernimmt nun die vollständige Kontrolle über die ID-Vergabe. In n8n wurde das Feld id aus dem Mapping entfernt.

2. Problem: Inkonsistente ID-Sortierung
Problem: Die IDs entsprachen nicht der zeitlichen Abfolge der Messungen (chronologische Sortierung).

Lösung: 1. Daten in eine temporäre Tabelle mit ORDER BY zeitstempel ASC gesichert. 2. Originaltabelle geleert. 3. Daten ohne IDs zurückgespielt, sodass PostgreSQL die IDs beim Einfügen neu und aufsteigend nach Zeit vergeben hat.



## 🤖 Workflow-Automatisierung (n8n)
1. Fehler: cannot insert a non-DEFAULT value into column "id"
Ursache: n8n hat versucht, einen Wert in das ID-Feld zu schreiben, obwohl die Datenbank auf GENERATED ALWAYS eingestellt war.

Lösung: Das Feld id im PostgreSQL-Node unter "Columns" komplett gelöscht. Nur noch Nutzdaten (Temperatur, Feuchtigkeit, Zeitstempel) werden gesendet.

2. Fehler: Column to match on not found in input item
Ursache: Der Node stand auf "Update" oder "Upsert", fand aber kein Abgleich-Feld (ID).

Lösung: Umstellung der Operation auf "Insert", da Sensor-Daten als fortlaufende Historie nur angehängt und nicht nachträglich verändert werden müssen.

## 📡 Hardware & Kommunikation (ESP32)
1. Fehler: [Errno 116] ETIMEDOUT
Problem: Der ESP32 verliert bei langen Intervallen (15 Min.) die Verbindung zum MQTT-Broker.

Ursache: Die Keepalive-Zeit des Brokers wurde während des time.sleep() überschritten.

Lösung: Implementierung des "Connect-Publish-Disconnect"-Musters. Der ESP32 baut die Verbindung nur kurz zum Senden auf und trennt sie vor der langen Pause sauber.

2. Fehler: Wrong boot mode detected (0xXX)!
Problem: Der Chip wechselt nicht automatisch in den Download-Modus zum Flashen.

Ursache: Fehlende Autoreset-Schaltung oder Timing-Probleme auf dem Board.

Lösung Wrong boot mode:
Wrong boot mode detected (0xXX)! The chip needs to be in download mode.
Communication with the chip works (the ROM boot log is detected), but it is not being reset into the download mode automatically.
To resolve this, check the autoreset circuitry (if your board has it), or try resetting into the download mode manually. 
See Manual Bootloader for instructions.

Manual Bootloader: https://docs.espressif.com/projects/esptool/en/latest/esp32/advanced-topics/boot-mode-selection.html#manual-bootloader
Depending on the kind of hardware you have, it may also be possible to manually put your ESP32 board into Firmware Download mode (reset).

For development boards produced by Espressif, this information can be found in the respective getting started guides or user guides. For example, to manually reset a development board, hold down the Boot button (GPIO0) and press the EN button (EN (CHIP_PU)).

## 📉 Visualisierung (Grafana)
1. Problem: Keine Daten im Dashboard sichtbar
Ursache: Falscher Zeitfilter (Time Range) in Grafana. Da der Sensor nur alle 15 Minuten sendet, ist das Standard-Fenster "Last 5 minutes" oft leer.

Lösung: Umstellung des Dashboards auf "Last 3 hours" oder "Last 24 hours". Aktivierung des Auto-Refreshs auf 1 Minute.

