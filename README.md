# 🚀 Professional IoT Data Pipeline: From Edge to Dashboard

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Dieses Projekt demonstriert eine vollständige, skalierbare End-to-End-IoT-Infrastruktur. Es visualisiert Echtzeit-Sensordaten eines ESP32, die über eine Cloud-Native-Architektur verarbeitet und gespeichert werden.

## 🏗 Systemarchitektur
Das System folgt einer modernen Schicht-Architektur (Layered Architecture):

1.  **Edge Layer:** ESP32 mit **DHT22-Sensor** (MicroPython). Erfassung von Temp/Hum alle 60s.
2.  **Transport Layer:** **MQTT (Eclipse Mosquitto)** als leichtgewichtiges Messaging-Protokoll.
3.  **Orchestration Layer:** **n8n** (Workflow-Automation) zur Transformation und Filterung.
4.  **Persistence Layer:** **PostgreSQL 15** (LXC-Container) zur relationalen Langzeitspeicherung.
5.  **Presentation Layer:** **Grafana** zur Echtzeit-Visualisierung und Analyse.



## 🛠 Technologie-Stack
- **Hardware:** ESP32 (powered by USB-C) + DHT22 Sensor.
- **Virtualisierung:** Proxmox VE (Host für VM und LXC).
- **Container:** Docker & Docker Compose (Ubuntu VM).
- **Automation:** n8n (Low-Code Integration).
- **Database:** PostgreSQL im dedizierten LXC-Container.
- **Visualisierung:** Grafana Dashboarding.

## 📦 Repository-Struktur
```text
.
├── esp32/               # MicroPython Source Code (boot.py, main.py)             
├── infrastructure/      # docker-compose.yml & Konfigurations-Dateien
├── database/            # SQL-Schema (schema.sql)
├── docs/                # Troubleshooting & Quellen
├── images/              # Bilder
├── files/               # zusätzliche Dateien (.bin)
├── .env.example         # Vorlage für Umgebungsvariablen (KEINE PASSWÖRTER)
├── .gitignore           # Ausschlussregeln für Git (Sicherheit!)
└── README.md            # Diese Dokumentation

```


## ESP32-WROOM Pinout

<p align="center">
  <img src="https://forum.arduino.cc/t/esp32-wroom-d32-dev-board-uart-flash-etc-question/1267145" alt="ESP32 Pinout Plan" width="600">
  <br>
  <em>Abbildung 1: Pin-Belegung des genutzten ESP-32 WROOM</em>
</p>