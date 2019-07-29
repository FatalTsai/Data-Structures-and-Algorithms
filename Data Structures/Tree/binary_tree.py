def binarytree(root):
    return [root,[],[]]

def insertleft(root, newbranch):
    t = root.pop(1)
    if len(t)> 1:
        root.insert(1,[newbranch, t, []])
    else:
        root.insert(1,[newbranch, [], []])
    return t

def insertright(root, newbranch):
    t = root.pop(2)
    if len(t) >1:
        root.insert(2,[newbranch, [], t])
    else:
        root.insert(2,[newbranch, [], []])
    return t

def getrootval(root):
    return root[0]

def setrootval(root):
    root[0]= newval

def getleftchild(root):
    return root[1]

def getrightchild(root):
    return root[2]



r = binarytree(2)
insertleft(r,3)
insertleft(r,4)
insertright(r,5)
insertright(r,6)
print(r) #[2, [4, [3, [], []], []], [6, [], [5, [], []]]]


tree = binarytree('a')
insertleft(tree, 'b')
insertright(tree, 'c')
insertright(getrightchild(tree), 'd')
insertleft(getrightchild(getrightchild(tree)),'e')
print(b) #['a', ['b', [], []], ['c', [], ['d', ['e', [], []], []]]]





