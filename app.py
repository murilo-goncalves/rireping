from flask import Flask, render_template, stream_with_context, render_template_string
from ping_analytics.ping_buffer import PingThread
from time import sleep

app = Flask(__name__)

BUFFER_SIZE = 10
ping_buffer = [0 for _ in range(BUFFER_SIZE)]

@app.route('/')
def index():
    try: 
        return render_template('index.html')
    except Exception as e:
        return str(e)

@app.route("/stream")
def stream():
    tp = PingThread(ping_buffer, BUFFER_SIZE)
    tp.start()
    def get_latest_ping():
        while True:
            yield str(ping_buffer[BUFFER_SIZE-1]) + " "
            sleep(1)

    return app.response_class(get_latest_ping(), mimetype="text/plain")
