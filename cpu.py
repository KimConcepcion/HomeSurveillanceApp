
import psutil as ps

class CPU():
    
    threads = 0
    cores = 0
    avg_prc = 0
    cur_prc = 0
    frq = 0
    cur_frq = 0.0
    min_frq = 0.0
    max_frq = 0.0
    
    ##    Constructor:
    def __init__(self):
        self.threads = ps.cpu_count(logical=True)
        self.cores = ps.cpu_count(logical=False)
        self.frq = ps.cpu_freq(percpu=True)
        self.min_frq = self.frq[0][1]
        self.max_frq = self.frq[0][2]
    
    ##    Get average cpu load:
    def get_cpu_load(self):
        cpu_average_load = list()
        for i in range(5):
            cpu_average_load.append( ps.cpu_percent(0.5, percpu=False) )
        return cpu_average_load
    
    ##    Get current cpu load in percent:
    def get_current_cpu_percent(self):
        return ps.cpu_percent(1, percpu=False)
    
    ##    Get current cpu frequency:
    def get_current_cpu_frequency(self):
        val = ps.cpu_freq(percpu=True)
        return val[0][0]