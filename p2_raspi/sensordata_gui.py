# For MQTT
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




# Define Plot
xar = [] # Ordered list of temperature values
yar = [] # Ordered list of timestamps
style.use('bmh')
fig = plt.figure(figsize=(14, 4.5), dpi=100)
ax1 = fig.add_subplot(1, 1, 1)
ax1.set_ylim(0, 50)
line, = ax1.plot(xar, yar, 'b', marker='x')


# Define Function to add/animate Graph
def animate(temperature, timestamp):
    yar.append(temperature)
    xar.append(timestamp)
    line.set_data(xar, yar)
    ax1.set_xlim(0, timestamp)

plotcanvas = FigureCanvasTkAgg(fig, root)
plotcanvas.get_tk_widget().grid(column=1, row=1)
ani = animation.FuncAnimation(fig, animate, interval=1000, blit=False)

root.mainloop()