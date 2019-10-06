
import psutil as ps

class Memory():
    
    ##    Virtual memory attributes:
    vir_total = 0
    vir_available = 0
    vir_free = 0
    vir_used = 0
    vir_cached = 0
    vir_shared = 0
    
    ##    Swap memory attributes:
    swap_total = 0
    swap_used = 0
    swap_free = 0
    swap_sin = 0
    swap_sout = 0
    
    ##    VIRTUAL MEMORY
    def get_total_vir_memory(self):
        val = ps.virtual_memory()
        #return bytes2human(val.total)
        return round(val.total / 1024000)
    
    def get_available_vir_memory(self):
        val = ps.virtual_memory()
        #return bytes2human(val.available)
        return round(val.available / 1024000)
    
    def get_free_vir_memory(self):
        val = ps.virtual_memory()
        #return bytes2human(val.free)
        return round(val.free / 1024000)
    
    def get_used_vir_memory(self):
        val = ps.virtual_memory()
        #return bytes2human(val.used)
        return round(val.used / 1024000)
    
    def get_cached_memory(self):
        val = ps.virtual_memory()
        #return bytes2human(val.cached)
        return round(val.cached / 1024000)
    
    def get_shared_memory(self):
        val = ps.virtual_memory()
        #return bytes2human(val.shared)
        return round(val.shared / 1024000)
    
    ##    SWAP MEMORY
    def get_total_swap_memory(self):
        val = ps.swap_memory()
        #return bytes2human(val.total)
        return round(val.total / 1024000)
    
    def get_used_swap_memory(self):
        val = ps.swap_memory()
        #return bytes2human(val.used)
        return round(val.used / 1024000)
    
    def get_free_swap_memory(self):
        val = ps.swap_memory()
        #return bytes2human(val.free)
        return round(val.free / 1024000)
    
    def get_sin(self):
        val = ps.swap_memory()
        #return bytes2human(val.sin)
        return round(val.sin / 1024000)
    
    def get_sout(self):
        val = ps.swap_memory()
        #return bytes2human(val.sout)
        return round(val.sout / 1024000)