import dht
from machine import Pin, reset
import time
from umqtt.simple import MQTTClient
import json
import secrets

# 1. Konfiguration
MQTT_BROKER = secrets.MQTT_HOST
CLIENT_ID = "esp32_sensor_01"
TOPIC = "sensor/climate"

sensor = dht.DHT22(Pin(2))
led = Pin(2, Pin.OUT)

# Das Client-Objekt EINMAL außerhalb der Schleife
client = MQTTClient(CLIENT_ID, MQTT_BROKER, keepalive=60)

print("System gestartet. Warte auf erste Messung...")

while True:
    try:
        # 1. Sensor auslesen (DHT22 braucht etwas Zeit zum Aufwachen)
        time.sleep(2) 
        sensor.measure()
        t = sensor.temperature()
        h = sensor.humidity()
        
        # 2. Verbindung aufbauen (On-Demand)
        print("Verbinde mit Broker...")
        client.connect()
        
        # 3. Payload erstellen & Senden
        payload = json.dumps({"temp": t, "hum": h})
        client.publish(TOPIC, payload)
        print(f"Gesendet: {payload}")
        
        # Kurzes LED-Feedback
        led.value(1); time.sleep(0.2); led.value(0)
        
        # 4. Verbindung sauber TRENNEN (Wichtig für lange Pausen!)
        client.disconnect()
        print("Verbindung getrennt. Schlafe für 1 Minute...")
        
        # 5. Pause
        time.sleep(60)
        
    except Exception as e:
        print("Fehler im Ablauf:", e)
        # Bei Fehlern (z.B. WLAN weg) 10 Sekunden warten und dann ESP neu starten
        # Ein Neustart ist im Feld oft sicherer als endloses Reconnect-Gefummel
        time.sleep(10)
        reset()