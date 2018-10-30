def TreeInsert(tree, numero):
    pos = 0
    y = None
    x = tree[pos]
    while x != "":
        y = tree[pos]
        if numero < x:
            pos = (pos+1)*2-1
            x = tree[(pos+1)*2-1]
        else:
            pos = ((pos + 1) * 2)
            x = tree[((pos + 1)*2)]
    if y == None:
        tree[0] = numero
    else:
        tree[pos] = numero