from paho.mqtt import client as mqtt_client
import datetime
import time
from DHT_Sensor import DHTSensor

# Setup MQTT
MQTT_PORT=1883
MQTT_ADDRESS="127.0.0.1"
MQTT_CLIENT_NAME="Gruppe6_PiPub"
MQTT_TOPIC="dht11/temp"

while True:
    # Fetch Values
    temp_value = DHTSensor().dht_read_temp()
    timestamp = datetime.datetime.now().isoformat()
    text = f"{temp_value}_{timestamp}"
    print(text)

    #Send Text to MQTT
    client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION1,MQTT_CLIENT_NAME)
    client.connect(MQTT_ADDRESS, MQTT_PORT)
    client.publish(MQTT_TOPIC, text)

    time.sleep(5)
