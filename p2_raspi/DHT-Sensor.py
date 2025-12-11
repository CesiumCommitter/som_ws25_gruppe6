import time
import board
import adafruit_dht

class DHTSensor:
    def __init__(self, pin=board.D23):
        # Initialisieren Sie das dht-Gerät, wobei der Datenpin mit Pin 16 (GPIO 23) des Raspberry Pi verbunden ist:
        # dhtDevice = adafruit_dht.DHT11(board.D23)
        self.device = adafruit_dht.DHT11(pin)

    def dht_read(self):
        while True:
            try:
                temperature_c = self.device.temperature
                # temperature_f = temperature_c * (9 / 5) + 32
                humidity = self.device.humidity
                # print("Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(temperature_f, temperature_c, humidity))
                return temperature_c, humidity
            except RuntimeError as error:
                # Fehler passieren ziemlich oft, DHT's sind schwer zu lesen, einfach weitermachen
                print(error.args[0])
                time.sleep(2.0)
                continue
            except Exception as error:
                self.device.exit()
                time.sleep(2.0)
                raise error
