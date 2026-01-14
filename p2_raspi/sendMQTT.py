from paho.mqtt import client as mqtt_client
import datetime
import time
from DHT_Sensor import DHTSensor
from random import randint

# setup MQTT
MQTT_PORT=1883
MQTT_ADDRESS="127.0.0.1"
MQTT_CLIENT_NAME="Gruppe6_PiPub"
MQTT_TOPIC="dht11/temp"

# create an instance of the sensor class
sensor = DHTSensor()

# create an instance of the paho.mqtt client class. connect to MQTT
client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION1, MQTT_CLIENT_NAME)
client.connect(MQTT_ADDRESS, MQTT_PORT)

while True:
    # fetch Values
    temp_value = sensor.dht_read_temp()
    humid_value = sensor.dht_read_humidity()
    timestamp = datetime.datetime.now().isoformat()
    text = f"{temp_value}_{humid_value}_{timestamp}"

    # Publish Message
    client.publish(MQTT_TOPIC, text)        # send text to MQTT

    # wait 5 sec.
    time.sleep(5)
