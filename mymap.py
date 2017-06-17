class LinearMap:
    """Represents a mapping from key to value."""
    def __init__(self):
        self.items = []
        
    def __str__(self):
        return str(self.items)
        
    def add(self, k, v):
        self.items.append((k,v))
        
    def get(self, k):
        for key, value in self.items:
            if key == k:
                return value 
            else: 
                raise KeyError
            

class BetterMap:
    def __init__(self, n=100):
        self.maps = []
        for i in range(n):
            self.maps.append(LinearMap())
            
    def __str__(self):
        return str(self.maps)
        
    def find_map(self, k):
        """Find map in list of LinearMaps.
        
        Using hash function to generate index of LinearMap.
        
        returns: found map.  
        """
        index = hash(k) % len(self.maps)
        return self.maps[index]
        
    def add(self, k, v):
        m = self.find_map(k)
        m.add(k, v)
        
    def get(self, k):
        m = self.find_map(k)     
        return m.get(k)   
        
        

def HashMap:
    """Represents a hash map.
    
    attributes: num, add(), get(), resize()
    """
    def __init__(self, n=2):
        self.maps = BetterMap(n)
        self.num = 0
        
    def get(self, k):
        return self.maps.get(k) 
        
    def add(self, k, v):
        if self.num == len(self.maps.maps):
            self.resize()  
                  
        self.maps.add(k, v)
        self.num += 1

    def resize(self):
        """Resize hash map.
        
        Create new map, rehash entries from old map and add to new map.
        """
        new_map = BetterMap(self.num*2)   
        for m in self.maps.maps:
            for k, v in m.items:
                new_map.add(k, v)
                
        self.maps = new_map                
                 
    
    

if __name__ == "__main__":
    d = LinearMap()
    d.add("name", "dika")
    d.add("sex", "male")
    print(d.get("name"))
    bd = BetterMap(4)
    bd.add("name", "Solomon")
    bd.add("sex", "Male")
    bd.add("height", "1.79m")
    print(bd)

                
        