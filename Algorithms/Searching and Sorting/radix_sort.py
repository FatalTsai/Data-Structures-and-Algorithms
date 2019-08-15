def countsort(arr):
    n = len(arr)
    max_value = max(arr)
    m = max_value +1
    count = [0] *m

    for x in arr:
        count[x] += 1
    i = 0
    for x in range(m):
        for y in range(count[x]):
            arr[i] = x
            i += 1
    return arr

def radixsort(arr):
    max1 = max(arr)
    exp = 1
    while max1/exp > 0:
        countsort(arr)
        exp *= 10
    

    
arr = [1,5,0,2,3,1,6,4]
radixsort(arr)
print(arr)