class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data

        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                nextslot = self.rehash_plusone(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash_plusone(nextslot, len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data

                else:
                    self.data[nextslot] = data


    def hashfunction(self, key, size):
        return key%size


    def rehash_plusone(self, oldhash, size):
        return (oldhash+1)%size


    def get(self, key):
        start = self.hashfunction(key, len(self.slots))

        data = None 
        stop = False
        found = False
        pos = start
        while self.slots[pos] != None and not found and not stop:
            if self.slots[pos] == key:
                found = True
                data = self.data[pos]
            else:
                pos = self.rehash_plusone(pos, len(self.slots))
                if pos == start:
                    stop = True
        return data

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)


#example
H = HashTable(size= 11)
H[54] = 'make'
H[26] = 'run'
H[72] = 'hit'
H[17] = 'take'
H[32] = 'converse'
H[44] = 'gain'
H[82] = 'experience'
print(H.slots)
print(H.data)

print(H.get(26))

H.put(4, 'see')
print(H.slots)
print(H.data)






