class treenode:
    def __init__(self, key, val, left= None, right= None, par= None): 
        self.key = key
        self.payload = val
        self.leftchild = left  
        self.rightchild = right 
        self.par = par   #par: parent 

    def haslch(self):
        return self.leftchild

    def hasrch(self):
        return self.rightchild

    def islch(self):
        return self.par and self.par.leftchild == self

    def isrch(self):
        return self.par and self.par.rightchild == self

    def isroot(self):
        return not self.par

    def isleaf(self):
        return not (self.leftchild or self.rightchild)

    def hasanych(self):
        return self.leftchild or self.rightchild

    def hasbothch(self):
        return self.leftchild and self.rightchild

    def spliceout(self):
        if self.isleaf():
            if self.islch():
                self.par.leftchild = None
            else:
                self.par.rightchild = None
        elif self.hasanych():
            if self.haslch():
                if self.islch():
                    self.par.leftchild = self.leftchild
                else:
                    self.par.rightchild = self.leftchild
                self.leftchild.par = self.par
            else:
                if self.islch():
                    self.par.leftchild = self.rightchild
                else:
                    self.par.rightchild = self.rightchild
                self.rightchild.par = self.par

    def findsc(self):
        sc = None
        if self.hasrch():
            sc = self.rightchild.findmin()
        else:
            if self.par:
                if self.islch():
                    sc = self.par
                else:
                    self.par.rightchild = None
                    sc = self.par.findsc()
                    self.par.rightchild = self
        return sc

    def findmin(self):
        curr = self
        while curr.haslch():
            curr = curr.leftchild
        return curr

    def replacenode(self, key, val, lc, rc):
        self.key = key
        self.val = val
        self.leftchild = lc
        self.rightchild = rc
        if self.haslch():
            self.leftchild.par = self
        if self.hasrch():
            self.rightchild.par = self

class binarysearchtree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    #def __iter__(self):
    #    return self.root.__iter__()

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root= treenode(key, val)
        self.size += 1

    def _put(self, key, val, cn):
        if key < cn.key:
            if cn.haslch():
                self._put(key, val, cn.leftchild)
            else:
                cn.leftchild = treenode(key, val, par = cn)
        else:
            if cn.hasrch():
                self._put(key,val,cn.rightchild)
            else:
                cn.rightchild = treenode(key, val, par= cn)
    '''
    # AVL tree
    def _put(self, key, val, cn):
        if key < cn.key:
            if cn.haslch():
                self._put(key, val, cn.leftchild)
            else:
                cn.leftchild = treenode(key, val, par = cn)
                self.updatebalance(cn.leftchild)
         else:
            if cn.hasrch():
                self._put(key,val,cn.rightchild)
            else:
                cn.rightchild = treenode(key, val, par= cn)
                self.updatebalance(cn.rightchild)
     
    def updatebalance(self, node):
        if node.balancefactor >1 or node.balancefactor < -1:
            self.rebalance(node)
            return
        if node.parent != None:
            if node.islch():
                node.par.balancefactor += 1
            elif node.isrch():
                node.par.balancefactor -= 1
            if node.par.balancefactor != 0:
                self.updatebalance(node.par)
              
    def rotateleft(self, rotroot):
        newroot = rotroot.rightchild
        rotroot.rightchild = newroot.leftchild
        if newroot.leftchild != None:
            newroot.leftchild.par = rotroot
        newroot.par = rotroot.par
        if rotroot.isroot():
            self.root = newroot
        else:
            if rotroot.isleftchild():
                rotroot.par.leftchild = newroot
            else:
                rotroot.par.rightchild = newroot
        newroot.leftchild = rotroot
        rotroot.par = newroot
        rotroot.balancefactor = rotroot.balancefactor + 1 - min(newroot.balancefactor, 0)
        newroot.balancefactor = newroot.balancefactor + 1 + max(rotroot.balancefactor, 0)
    
    '''
    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, cn): #cn: current node
        if not cn:
            return None
        elif cn.key == key:
            return cn
        elif key < cn.key:
            return self._get(key, cn, leftchild)
        else:
            return self._get(key, cn, rightchild)

    def __getitem__(self, key):
        return self.get(key)

    def __cointains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            nodetoremove= self._get(key, self.root)
            if nodetoremove:
                self.remove(nodetoremove)
                self.size -= 1
            else:
                raise KeyError("Error, key not in the tree")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError("Error, key not in the tree")

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, cn):
        if cn.isleaf(): 
            if cn == cn.par.leftchild:
                cn.par.leftchild = None
            else:
                cn.par.rightchild = None
        elif cn.hasbothch():
            sc = cn.findsc()
            sc.spliceout()
            cn.key = sc.key
            cn.payload = sc.payload
            
        else: # this node has one child
            if cn.haslch():
                if cn.islch():
                    cn.leftchild.par = cn.par
                    cn.par.leftchild = cn.leftchild
                elif cn.isrch():
                    cn.leftchild.par = cn.par
                    cn.par.leftchild = cn.leftchild
                else:
                    cn.replacenode(cn.leftchild.key, cn.leftchild.payload,
                        cn.leftchild.leftchild, cn.leftchild.rightchild)
            else:
                if cn.islch():
                    cn.rightchild.par = cn.par
                    cn.par.leftchild = cn.rightchild
                elif cn.isrch():
                    cn.rightchild.par = cn.par
                    cn.par.rightchild = cn.rightchild
                else:
                    cn.replacenode(cn.rightchild.key, cn.rightchild.payload,
                        cn.rightchild.leftchild, cn.rightchild.rightchild)





tree = binarysearchtree()
tree[3]="one"
tree[7]="two"
tree[5]="three"













