from flask import Flask, render_template
import psutil as ps

app = Flask(__name__)

## Network stuff:
HOST = '192.168.1.34'
#HOST = 'localhost'
PORT = '5000'

## CPU Specs:
cpu_threads = ps.cpu_count(logical=True)
cpu_cores = ps.cpu_count(logical=False)

## CPU Percent:
#cpu_prc = ps.cpu_percent(1, percpu=True)
cpu_avg_prc = ps.cpu_percent(1, percpu=False)

## Frequency in GHz (Originally in MHz):
cpu_frq = ps.cpu_freq(percpu=True)
current_frq = cpu_frq[0][0] / 1000
min_frq = cpu_frq[0][1] / 1000
max_frq = cpu_frq[0][2] / 1000

## Index Route:
@app.route('/')
def index():
    return render_template(
        'index.html',
        threads=cpu_threads, cores=cpu_cores, current_speed=current_frq, cpu_average_load=cpu_avg_prc
        )
    
## Error Route:
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')

## Start server:
if __name__ == '__main__':
    print('Starting server')
    app.run(host=HOST, port=PORT)
