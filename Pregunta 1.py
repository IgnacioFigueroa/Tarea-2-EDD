def TreeInsert(tree, number):
    pos = 0
    y = None
    x = tree[pos]
    while x != "":
        y = tree[pos]
        if number < x:
            pos = (pos+1)*2-1 #izquierda
            x = tree[pos]
        else:
            pos = ((pos + 1) * 2) #derecho
            print (pos)
            x = tree[pos]
            print (x)
    if y == None:
        tree[0] = number
    else:
        tree[pos] = number
    return tree

def RotationLeft(tree, positionx):
    positiony = (positionx+1)*2
    valuey = tree[positiony]
    tree[(positionx+1)*2] = tree[(positiony+1)*2-1] #right[x] = left[y]




