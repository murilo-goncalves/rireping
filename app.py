from flask import Flask, render_template
from ping_analytics.ping_buffer import PingThread
import pygal

app = Flask(__name__)

BUFFER_SIZE = 10
ping_buffer = [0 for _ in range(BUFFER_SIZE)]

@app.route('/')
def index():
    try: 
        pt = PingThread(ping_buffer, BUFFER_SIZE)
        pt.start()
        ping_chart = pygal.Line()
        ping_chart.title = "Rirep's ping"
        ping_chart.x_labels = map(str, range(10))
        ping_chart.y_labels = range(0, 100, 10)
        ping_chart.add('Ping', ping_buffer)
        ping_chart_data = ping_chart.render_data_uri()
        return render_template('index.html', ping_chart_data=ping_chart_data)
    except Exception as e:
        return str(e)
