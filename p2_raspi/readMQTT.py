from paho.mqtt import client as mqtt_client
import time

MQTT_PORT = 1883
MQTT_ADDRESS = "141.22.36.200"
MQTT_CLIENT_NAME = "Gruppe6_PiSub"
MQTT_TOPIC = "Gruppenname/Kanal"
TICK_RATE_HZ = 2
TICK_RATE = 1/TICK_RATE_HZ


message_queue = []

def on_message(client, userdata, msg):
    message=msg.payload.decode()
    message_queue.append(message)

client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION1,MQTT_CLIENT_NAME)
client.connect(MQTT_ADDRESS,MQTT_PORT)
client.subscribe(MQTT_TOPIC)
client.on_message = on_message
client.loop_start()

while (True):
    last_value=""
    value_queue = []
    time.sleep(TICK_RATE)
    while len(message_queue)>0:
        last_value=message_queue.pop()
        value_queue.append(last_value)
        #print(last_value)
        
        