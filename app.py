from flask import Flask, render_template
import psutil as ps

app = Flask(__name__)

## Network stuff:
#HOST = '192.168.1.34'
HOST = 'localhost'
PORT = '5000'

## Static CPU info:
cpu_threads = ps.cpu_count(logical=True)
cpu_cores = ps.cpu_count(logical=False)

def get_cpu_load():
    cpu_average_load = list()
    
    for i in range(5):
        cpu_average_load.append( ps.cpu_percent(1, percpu=False) )
    return cpu_average_load

## Index Route:
@app.route('/', methods=['GET'])
def index():

    ## Dynamic CPU Info - Update per request:
    cpu_avg_prc = get_cpu_load()
    cpu_current_avg_prc = ps.cpu_percent(1, percpu=False)
    
    cpu_frq = ps.cpu_freq(percpu=True)
    current_frq = cpu_frq[0][0]
    
    return render_template(
        'index.html', 
        threads=cpu_threads, cores=cpu_cores, current_speed=current_frq, cpu_average_load=cpu_current_avg_prc,
        cpu_avg_load_0=cpu_avg_prc[0], cpu_avg_load_1=cpu_avg_prc[1], cpu_avg_load_2=cpu_avg_prc[2], 
        cpu_avg_load_3=cpu_avg_prc[3], cpu_avg_load_4=cpu_avg_prc[4]
        )

## Error Route:
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')

## Start server:
if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=False)