# For MQTT
import datetime
import tkinter
from paho.mqtt import client as mqtt_client

# For GUI
from tkinter import *
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Define MQTT Source
MQTT_PORT = 1883
MQTT_ADDRESS = "141.22.36.200"
MQTT_CLIENT_NAME = "Gruppe6_PiSub_Sammy"
MQTT_TOPIC = "dht11/temp"


# Start MQTT Listening
message_queue = []
def on_message(client, userdata, msg):
    message = msg.payload.decode()
    message_queue.append(message)
client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION1, MQTT_CLIENT_NAME, clean_session=True)
client.on_message = on_message
client.connect(MQTT_ADDRESS, MQTT_PORT, keepalive=60)
client.subscribe(MQTT_TOPIC)
client.loop_start()


# Define GUI
root = Tk()
root.geometry('1200x700+200+100')
root.title('DHT11 Sensor Data Visualisation')
root.state('zoomed')
root.config(background='#fafafa')


# Define Variables holding data
xar = [] # Ordered list of timestamps
yar = [] # Ordered list of temperature values
xar2 = [] # Ordered list of timestamps
yar2 = [] # Ordered list of humidity values


# Define Matplotlib Figure Style
style.use('bmh')
fig = plt.figure(figsize=(14, 4.5), dpi=100)


# Define Plot 1
ax1 = fig.add_subplot(2, 1, 1)
ax1.set_ylim(0, 50)
ax1.set_title("Temperature over Time")
line1, = ax1.plot(xar, yar, 'b', marker='x')


# Define Plot 2
ax2 = fig.add_subplot(2, 1, 2)
ax2.set_ylim(0, 100)
ax2.set_title("Humidity over Time")

line2, = ax2.plot(xar2, yar2, 'r', marker='o')


# Define List to iterate the animation over
value_queue = []


# Define Function to add/animate Graph
def animate(i):
    while len(message_queue)>0:

        # Fetch encoded Value
        last_value = message_queue.pop()
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
        line1.set_data(xar, yar)
        ax1.set_xlim(xar[0], timestamp_obj)

        # Update Graph 2
        yar2.append(int_humidity)
        xar2.append(timestamp_obj)
        line2.set_data(xar2, yar2)
        ax2.set_xlim(xar2[0], timestamp_obj)


plotcanvas = FigureCanvasTkAgg(fig, root)
plotcanvas.get_tk_widget().pack(expand=True, fill=tkinter.BOTH)
ani = animation.FuncAnimation(fig, animate, interval=1000, blit=False)


root.mainloop()
