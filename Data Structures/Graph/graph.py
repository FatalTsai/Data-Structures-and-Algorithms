class vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addneighbor(self,nbr,weight= 0):
        self.connectedTo[nbr] = weight
    
    def __str__(self):
        return str(self.id) + "connected To:" + str([x.id for x in self.connectedTo])
    
    def getconnections(self):
        return self.connectedTo.keys()
    
    def getid(self):
        return self.id

    def getweight(self):
        return self.connectedTo[nbr]
    
class graph:
    def __init__(self):
        self.vertlist= {}
        self.numvert= 0

    def addvertex(self,key):
        self.numvert += 1
        newvert = vertex(key)
        self.vertlist[key] = newvert
        return newvert
    
    def getvertex(self,n):
        if n in self.vertlist:
            return self.vertlist[n]
        else:
            return None
    
    def __contains__(self,n):
        return n in self.vertlist
    
    def addedge(self,from_,to_,cost=0):
        if from_ not in self.vertlist:
            nv= self.addvertex(from_)
        if to_ not in self.vertlist:
            nv= self.addvertex(to_)
        self.vertlist[from_].addneighbor(self.vertlist[to_],cost)
    
    def getvertices(self):
        return self.vertlist.keys()
    
    def __iter__(self):
        return iter(self.vertlist.values())
    
