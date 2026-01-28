import network
import time
import secrets # importiert Inhalt aus secrets.py

def do_connect(): # Funktion zum Verbinden mit dem WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Verbinde mit Netzwerk...')
        wlan.connect(secrets.WIFI_SSID, secrets.WIFI_PASS)
        
        # 10 Sekunden lang zu verbinden
        attempt = 0
        while not wlan.isconnected() and attempt < 10:
            time.sleep(1)
            attempt += 1
            
    if wlan.isconnected(): # Fehler IF-Schleife
        print('WLAN verbunden! Netzwerk-Konfiguration:', wlan.ifconfig())
    else:
        print('WLAN Verbindung fehlgeschlagen!')

do_connect()