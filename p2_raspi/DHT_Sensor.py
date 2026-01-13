import time
import board
import adafruit_dht
from pulseio import PulseIn

class DHTSensor:
    def __init__(self):
        self.device = adafruit_dht.DHT11(board.D23, use_pulseio=False)

    def dht_read_temp(self):
        while True:
            try:
                temperature_c = self.device.temperature
                return temperature_c
            except RuntimeError as error:
                print(error.args[0])
                time.sleep(2.0)
                continue
            except Exception as error:
                self.device.exit()
                raise error
            time.sleep(2.0)

    def dht_read_humidity(self):
        while True:
            try:
                humidity = self.device.humidity
                #print(f"Humidity: {humidity}%")
                return humidity
            except RuntimeError as error:
                # Fehler passieren ziemlich oft, DHT's sind schwer zu lesen, einfach weitermachen
                print(error.args[0])
                time.sleep(2.0)
                continue
            except Exception as error:
                self.device.exit()
                raise error
            time.sleep(2.0)