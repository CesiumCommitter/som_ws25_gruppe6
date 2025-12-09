from bottle import route, run
import threading, time

def background_server_function(name):
    run(host='0.0.0.0', port=80, debug=True)

@route('/hello')
def hello():
    return "Hello Class SOM WiSe 2025!"

threading.Thread(target=background_server_function, args=(1,), daemon=True).start()
while True:
    print("Mainloop is here.")
    time.sleep(1)