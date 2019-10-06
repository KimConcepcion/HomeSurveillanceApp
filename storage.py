
import psutil as ps

class Storage():
    
    def get_total_storage(self):
        return round( (ps.disk_usage('/').total / 1000000000),2 )
    
    def get_used_storage(self):
        return round( (ps.disk_usage('/').used / 1000000000),2 )
    
    def get_free_storage(self):
        return round( (ps.disk_usage('/').free / 1000000000),2 )
