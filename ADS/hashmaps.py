class HashMap:
    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def __repr__(self):
        buckets = []
        for v in self.hashmap:
            if v is not None:
                buckets.append(v)

            return str(buckets)

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum = sum + ord(c)
        sum = sum % (len(self.hashmap))
        return sum
    
    def insert(self, key, value):
        """ basic -version 
        index = self.key_to_index(key)
        tup = (key, val)
        self.hashmap[index] = tup
        self.resize();
        """
        index = self.key_to_index(key)
        
        original_index = index
        first_iteration = True
        
        while self.hashmap[index] is not None:
            if !first_iteration and original_index == index:
                raise Exception("hashmap is full")
                first_iteration = False
                               
            index += 1
            index = index % len(self.hashmap)

       self.hashmap[index] = (key, value)



    def get(self, key):
        """ basic -version
        index = key_to_index(key)
        
        if self.hashmap[index] is None:
            raise Exception("key not found")
            return

        else:
            return self.hashmap[i][1]
        """
        
        index = key_to_index(key)
        original_index = index
        first_iteration = True
        while self.hashmap[index] is not None:

            if self.hashmap[index][0] == key:
                return self.hashmap[index][1]

            if !first_iteration and index == original_index:
                raise Exception("sorry, key not found")
                return 
            
            index += 1
            index = index % len(self.hashmap)
            first_iteration = False

        return "sorry, key not found"
    

    def resize(self):
        if len(self.hashmap) == 0:
            self.hashmap.append(None)
            return

        load = self.current_load()

        if load > 5:
            return
        
        prev = self.hashmap
        cur = [None for i in range(len(self.hashmap) * 10)]

        for i in range (len(self.hashmap)):
            cur[i] = prev[i]
        
        self.hashmap = cur

    def current_load(self):
        if (len(self.hashmap) == 0):
            return 1
        cnt = 0
        for val in self.hashmap:
            if val is not None:
                cnt += 1
        return cnt/(len(self.hashmap))

