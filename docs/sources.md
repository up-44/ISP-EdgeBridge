# Quellen- und Ressourcenverzeichnis
Dieses Projekt nutzt eine Vielzahl an Open-Source-Technologien und professionellen Tools. Nachfolgend sind die primären Ressourcen aufgeführt, die für die Entwicklung, Virtualisierung und Datenverarbeitung genutzt wurden.

## Hardware & Firmware

- Generische MicroPython-Firmware für ESP32 (WROOM): [micropython.org](https://micropython.org/download/ESP32_GENERIC/)
- Espressif Esptool	als Bootloader-Utility zum Flashen des ESP32: [docs.espressif.com](https://docs.espressif.com/projects/esptool)
- MicroPython Library	umqtt.simple für die MQTT-Kommunikation: [micropython-lib](https://github.com/micropython/micropython-lib)


## Entwicklungswerkzeuge

- Visual Studio Code: Primärer Editor für die MicroPython-Entwicklung. [code.visualstudio.com] (https://code.visualstudio.com/)

- Python: Basis-Laufzeitumgebung für lokale Skripte und Paketverwaltung. [python.org] (https://www.python.org/)

- PIP: Paketmanager für Python-Bibliotheken.  [pypi.org] (https://pypi.org/project/pip/)

- DBeaver: Universelles Datenbank-Werkzeug zur Verwaltung von PostgreSQL.  [dbeaver.io] (https://dbeaver.io/)


## Infrastruktur & Virtualisierung

- Proxmox VE: Plattform für die Bereitstellung der LXC-Container.  [proxmox.com] (https://www.proxmox.com/)

- Ubuntu Server: Betriebssystem für die Docker-Instanzen.  [ubuntu.com] (https://ubuntu.com/download/server)

- Docker & Compose: Container-Virtualisierung für n8n und Grafana.  [docker.com] (https://www.docker.com/)


## Backend & Analyse-Tools

- PostgreSQL: Relationale Datenbank zur persistenten Speicherung der Sensordaten.  [postgresql.org] (https://www.postgresql.org/)

- n8n: Low-Code Workflow-Automatisierung für das MQTT-Processing. [n8n.io] (https://n8n.io/)

- Grafana: Dashboard-Lösung zur Visualisierung der Messreihen.  [grafana.com] (https://grafana.com/)