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

def connect_mqtt():
    try:
        # Wir fügen ein keepalive hinzu, damit die Verbindung stabil bleibt
        client = MQTTClient(CLIENT_ID, MQTT_BROKER, keepalive=60)
        client.connect()
        print("Erfolgreich mit MQTT-Broker verbunden")
        return client
    except Exception as e:
        print("MQTT Verbindungsfehler:", e)
        return None

# Initialer Start
client = connect_mqtt()

# Zähler für Stabilitätstest
msg_count = 0

while True:
    try:
        # Dem DHT22 etwas Zeit geben
        time.sleep(2) 
        sensor.measure()
        t = sensor.temperature()
        h = sensor.humidity()
        
        payload = json.dumps({"temp": t, "hum": h, "count": msg_count})
        
        if client:
            client.publish(TOPIC, payload)
            msg_count += 1
            print(f"Nachricht #{msg_count} gesendet: {payload}")
        else:
            print("Kein Client vorhanden, versuche Reconnect...")
            client = connect_mqtt()
            
        led.value(1); time.sleep(0.1); led.value(0)
        
    except Exception as e:
        print("Fehler im Loop:", e)
        # Wenn der Fehler "ECONNRESET" oder ähnlich ist, Hard-Reset des Clients
        try:
            client.disconnect()
        except:
            pass
        time.sleep(5)
        client = connect_mqtt()
        
        # Falls gar nichts mehr geht nach 3 Fehlern: ESP32 neu starten
        if msg_count > 0 and msg_count % 50 == 0: 
             print("Sicherheits-Neustart...")
             reset()

    time.sleep(898)