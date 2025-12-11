from paho.mqtt import client as mqtt_client
from random import randint
import datetime
import D

MQTT_PORT=1883
MQTT_ADDRESS="127.0.0.1"
MQTT_CLIENT_NAME="Gruppe6_PiPub"
MQTT_TOPIC="dht11/temp"

# Fetch Values to send to MQTT
temp_value = str(randint(1, 100))
timestamp = datetime.datetime.now().isoformat()


# Hier entsteht die Nachricht
text = f"{temp_value}_{timestamp}"

#Send Text to MQTT
client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION1,MQTT_CLIENT_NAME)
client.connect(MQTT_ADDRESS, MQTT_PORT)
client.publish(MQTT_TOPIC, text)