from flask import Flask, render_template
from cpu import CPU
from memory import Memory

app = Flask(__name__)

#HOST = '192.168.1.34'
HOST = 'localhost'
PORT = '5000'
cpu = CPU()
mem = Memory()

## Index Route:
@app.route('/', methods=['GET'])
def index():

    ## CPU:
    cpu_avg_prc = cpu.get_cpu_load()
    cpu.cur_prc = cpu.get_current_cpu_percent()
    cpu.cur_frq = cpu.get_current_cpu_frequency()
    
    ## Memory:
    mem.vir_total = mem.get_total_vir_memory()
    mem.vir_available = mem.get_available_vir_memory()
    mem.vir_free = mem.get_free_vir_memory()
    mem.vir_used = mem.get_used_vir_memory()
    #mem.vir_cached = mem.get_cached_memory()
    #mem.vir_shared = mem.get_shared_memory()
    
    mem.swap_total = mem.get_total_swap_memory()
    mem.swap_used = mem.get_used_swap_memory()
    mem.swap_free = mem.get_free_swap_memory()
    mem.swap_sin = mem.get_sin()
    mem.swap_sout = mem.get_sout()
    
    print(mem.vir_available)
    
    return render_template(
        'status.html', 
        threads=cpu.threads, cores=cpu.cores, 
        current_speed=cpu.cur_frq, minimum_speed=cpu.min_frq, maximum_speed=cpu.max_frq, 
        cpu_average_load=cpu.cur_prc,
        cpu_avg_load_0=cpu_avg_prc[0], cpu_avg_load_1=cpu_avg_prc[1], cpu_avg_load_2=cpu_avg_prc[2], cpu_avg_load_3=cpu_avg_prc[3], cpu_avg_load_4=cpu_avg_prc[4],
        total_vir_mem=mem.vir_total, available_vir_mem=mem.vir_available, free_vir_mem=mem.vir_free, used_vir_mem=mem.vir_used, cached_vir_mem=mem.vir_cached, shared_vir_mem=mem.vir_shared,
        total_swap_mem=mem.swap_total, used_swap_mem=mem.swap_used, free_swap_mem=mem.swap_free, sin_mem=mem.swap_sin, sout_mem=mem.swap_sout
        )

## Error Route:
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')

## Start server:
if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=False)