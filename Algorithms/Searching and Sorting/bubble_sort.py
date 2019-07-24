def bubblesort(alist):
    exchange = True
    passnumber = len(alist)- 1
    while passnumber > 0 and exchange:
        exchange = False
        for i in range(passnumber):
            if alist[i] > alist[i+1]:
                exchange = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnumber = passnumber- 1
    return alist

alist = [6, 12, 26, 93, 77, 31, 44, 55, 20, 92, 56]
print(bubblesort(alist))
