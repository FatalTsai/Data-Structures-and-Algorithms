def heapify(arr, n, i):
    larg = i
    l = 2 * i + 1
    r = 2 * (i + 1)
    if l < n and arr[larg] < arr[l]:
        larg = l

    if r < n and arr[larg] < arr[r]:
        larg = r

    if larg != i:
        arr[i], arr[larg] = arr[larg],arr[i]
        heapify(arr, n, larg)

def buld_max_heap(arr, m):
    for i in range(m//2, -1, -1):
        heapify(arr, m, i)


def heapsort(arr):
    n = len(arr)
    buld_max_heap(arr, n)
    while n >0:
        arr[0], arr[n-1] = arr[n-1], arr[0]
        n -= 1
        heapify(arr, n, 0)
    return arr


arr = [2, 7, 26, -2, 5, 21, 3, 10]
heapsort(arr)
print(arr)





