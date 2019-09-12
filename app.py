from flask import Flask, render_template
import psutil as ps

app = Flask(__name__)

## Network stuff:
#HOST = '192.168.1.34'
HOST = 'localhost'
PORT = '5000'

## CPU stuff:
cpu_threads = ps.cpu_count(logical=True)
cpu_cores = ps.cpu_count(logical=False)
cpu_prc = ps.cpu_percent(interval=0.5, percpu=False)
cpu_frq = ps.cpu_freq(percpu=True)
cpu_temp = ps.sensors_temperatures(fahrenheit=False)

## Index Route:
@app.route('/')
def index():
    return render_template(
        'index.html',
        threads=cpu_threads, cores=cpu_cores, percent=cpu_prc, frequency=cpu_frq[0], temperature=cpu_temp
        )
    
## Error Route:
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')

## Start server:
if __name__ == '__main__':
    print('Starting server')
    app.run(host=HOST, port=PORT)