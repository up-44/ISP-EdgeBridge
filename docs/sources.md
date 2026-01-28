# Quellen- und Ressourcenverzeichnis
Dieses Projekt nutzt eine Vielzahl an Open-Source-Technologien und professionellen Tools. Nachfolgend sind die primären Ressourcen aufgeführt, die für die Entwicklung, Virtualisierung und Datenverarbeitung genutzt wurden.

## Hardware & Firmware

- MicroPython Firmware	Generische Firmware für ESP32 (WROOM)	micropython.org
- Espressif Esptool	Bootloader-Utility zum Flashen des ESP32	docs.espressif.com
- MicroPython Library	umqtt.simple für die MQTT-Kommunikation	micropython-lib



## Entwicklungswerkzeuge

- Visual Studio Code: Primärer Editor für die MicroPython-Entwicklung. code.visualstudio.com

- Python: Basis-Laufzeitumgebung für lokale Skripte und Paketverwaltung. python.org

- PIP: Paketmanager für Python-Bibliotheken. pypi.org

- DBeaver: Universelles Datenbank-Werkzeug zur Verwaltung von PostgreSQL. dbeaver.io


## Infrastruktur & Virtualisierung

- Proxmox VE: Plattform für die Bereitstellung der LXC-Container. proxmox.com

- Ubuntu Server: Betriebssystem für die Docker-Instanzen. ubuntu.com

- Docker & Compose: Container-Virtualisierung für n8n und Grafana. docker.com


## Backend & Analyse-Tools

- PostgreSQL: Relationale Datenbank zur persistenten Speicherung der Sensordaten. postgresql.org

- n8n: Low-Code Workflow-Automatisierung für das MQTT-Processing. n8n.io

- Grafana: Dashboard-Lösung zur Visualisierung der Messreihen. grafana.com