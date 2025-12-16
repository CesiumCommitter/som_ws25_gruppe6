""""
from bottle import route, run
import threading, time

def background_server_function(name):
    run(host='0.0.0.0', port=80, debug=True)

@route('/hello')
def hello():
    return "Hello Class çSOM WiSe 2025!"

threading.Thread(target=background_server_function, args=(1,), daemon=True).start()
while True:
    print("Mainloop is here.")
    time.sleep(1)
"""

from bottle import route, run, response
import threading, time, json, random

# Beispieldaten
temperature = []
humidity = []
timestamps = []

@route('/test')
def index():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Sensorwerte</title>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    </head>
    <body>
        <h2>Temperatur</h2>
        <canvas id="tempChart"></canvas>

        <h2>Luftfeuchtigkeit</h2>
        <canvas id="humChart"></canvas>

    <button
        onclick="window.location.href='/csv'"
        style="
            margin-top: 30px;
            padding: 15px 30px;
            font-size: 18px;
            cursor: pointer;
        ">
        CSV herunterladen
    </button>

        <script>
            async function loadData() {
                const res = await fetch('/data');
                const data = await res.json();

                tempChart.data.labels = data.time;
                tempChart.data.datasets[0].data = data.temp;

                humChart.data.labels = data.time;
                humChart.data.datasets[0].data = data.hum;

                tempChart.update();
                humChart.update();
            }

            const tempChart = new Chart(
                document.getElementById('tempChart'),
                {
                    type: 'line',
                    data: {
                        labels: [],
                        datasets: [{
                            label: 'Temperatur (°C)',
                            data: []
                        }]
                    }
                }
            );

            const humChart = new Chart(
                document.getElementById('humChart'),
                {
                    type: 'line',
                    data: {
                        labels: [],
                        datasets: [{
                            label: 'Luftfeuchtigkeit (%)',
                            data: []
                        }]
                    }
                }
            );

            setInterval(loadData, 1000);
        </script>
    </body>
    </html>
    """

@route('/data')
def data():
    response.content_type = 'application/json'
    return json.dumps({
        "time": timestamps,
        "temp": temperature,
        "hum": humidity
    })

@route('/csv')
def download_csv():
    response.content_type = 'text/csv'
    response.headers['Content-Disposition'] = 'attachment; filename="sensordaten.csv"'

    csv_data = "time,temperature,humidity\n"
    for t, temp, hum in zip(timestamps, temperature, humidity):
        csv_data += f"{t},{temp},{hum}\n"

    return csv_data

def background_server_function():
    run(host='0.0.0.0', port=80, debug=True)

def sensor_loop():
    while True:
        timestamps.append(time.strftime("%H:%M:%S"))
        temperature.append(20 + random.uniform(-1, 1))
        humidity.append(50 + random.uniform(-5, 5))

        # Speicher begrenzen
        timestamps[:] = timestamps[-20:]
        temperature[:] = temperature[-20:]
        humidity[:] = humidity[-20:]

        time.sleep(1)

threading.Thread(target=background_server_function, daemon=True).start()
threading.Thread(target=sensor_loop, daemon=True).start()

while True:
    print("Mainloop is here.")
    time.sleep(2)