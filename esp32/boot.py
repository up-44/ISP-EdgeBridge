import network
import time
import secrets

def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Verbinde mit Netzwerk...')
        wlan.connect(secrets.WIFI_SSID, secrets.WIFI_PASS)
        
        # Versuche 10 Sekunden lang zu verbinden
        attempt = 0
        while not wlan.isconnected() and attempt < 10:
            time.sleep(1)
            attempt += 1
            
    if wlan.isconnected():
        print('WLAN verbunden! Netzwerk-Konfiguration:', wlan.ifconfig())
    else:
        print('WLAN Verbindung fehlgeschlagen!')

do_connect()