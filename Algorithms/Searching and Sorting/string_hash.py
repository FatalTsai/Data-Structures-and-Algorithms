def hash(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
            sum += ((ord(astring[pos])) * (pos + 1))
    return print(sum%tablesize)


hash('cat', 11)
hash('max', 13)

