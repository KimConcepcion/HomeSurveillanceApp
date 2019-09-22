from flask import Flask, render_template
import psutil as ps

app = Flask(__name__)

## Network stuff:
HOST = '192.168.1.34'
#HOST = 'localhost'
PORT = '5000'

## Index Route:
@app.route('/')
def index():

    ## CPU Stuff - Update per request:
    cpu_threads = ps.cpu_count(logical=True)
    cpu_cores = ps.cpu_count(logical=False)
    cpu_avg_prc = ps.cpu_percent(1, percpu=False)
    cpu_frq = ps.cpu_freq(percpu=True)
    current_frq = cpu_frq[0][0]

    return render_template(
        'index.html', threads=cpu_threads, cores=cpu_cores, current_speed=current_frq, cpu_average_load=cpu_avg_prc
        )

## Error Route:
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')

## Start server:
if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=False)
