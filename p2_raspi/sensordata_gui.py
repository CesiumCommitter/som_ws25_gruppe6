# For MQTT
import datetime
import os
import random
import tkinter

from paho.mqtt import client as mqtt_client
import time


# For GUI
from tkinter import *
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Define MQTT Source
MQTT_PORT = 1883
MQTT_ADDRESS = "141.22.36.200"
MQTT_CLIENT_NAME = "Gruppe6_PiSub"
MQTT_TOPIC = "dht11/temp"
TICK_RATE_HZ = 2
TICK_RATE = 1/TICK_RATE_HZ


# Start MQTT Listening
message_queue = []
def on_message(client, userdata, msg):
    message = msg.payload.decode()
    message_queue.append(message)
client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION1, MQTT_CLIENT_NAME)
client.connect(MQTT_ADDRESS, MQTT_PORT)
client.subscribe(MQTT_TOPIC)
client.on_message = on_message
client.loop_start()


# Define GUI
root = Tk()
root.geometry('1200x700+200+100')
root.title('DHT11 Sensor Data Visualisation')
root.state('zoomed')
root.config(background='#fafafa')


# Define Plot 1
xar = [] # Ordered list of timestamps
yar = [] # Ordered list of temperature values
style.use('bmh')
fig = plt.figure(figsize=(14, 4.5), dpi=100)
ax1 = fig.add_subplot(1, 1, 1)
ax1.set_ylim(0, 50)
ax1.set_title("Temperature over Time")
line, = ax1.plot(xar, yar, 'b', marker='x')

# Define Plot 2
yar2 = [] # Ordered list of humidity values
ax2 = fig.add_subplot(2, 1, 2)
ax2.set_ylim(0, 100)
ax2.set_title("Humidity over Time")
line2, = ax2.plot(xar, yar2, 'r', marker='o')


# Define Starting variables
last_value = ""
value_queue = []
datetime_start = datetime.datetime.now()

# Define Function to add/animate Graph
def animate(i):
    while len(message_queue)>0:

        # Fetch encoded Value
        last_value=message_queue.pop()
        value_queue.append(last_value)

        # Decode Value
        vals = last_value.split("_", 3)
        int_temp = int(vals[0])
        int_humidity = int(vals[1])
        str_timestamp = vals[2]
        timestamp_obj = datetime.datetime.fromisoformat(str_timestamp)

        # Update Graph 1
        yar.append(int_temp)
        xar.append(timestamp_obj)
        line.set_data(xar, yar)
        ax1.set_xlim(xar[0], timestamp_obj)

        # Update Graph 2
        yar2.append(int_humidity)
        xar.append(timestamp_obj)
        line.set_data(xar, yar2)
        ax1.set_xlim(xar[0], timestamp_obj)


plotcanvas = FigureCanvasTkAgg(fig, root)
plotcanvas.get_tk_widget().pack(expand=True, fill=tkinter.BOTH)
ani = animation.FuncAnimation(fig, animate, interval=1000, blit=False)


root.mainloop()