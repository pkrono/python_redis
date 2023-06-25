import redis

class redis_cache():
    
    def __init__(self):
        pool = redis.ConnectionPool(host='localhost', port=6379,
                                    decode_responses=True)
        self.server = redis.Redis(connection_pool=pool)
    
    def set(self, key, value):
        return self.server.set(key, value)
        
    def get(self, key):
        return self.server.get(key)
    
    def get_all_keys(self):
        return self.server.keys()
        
        
if __name__ == '__main__':
    server = redis_cache()
    #server.set('name','Diyari')
    print(server.get_all_keys())