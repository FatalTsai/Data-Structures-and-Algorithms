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

arr = [3,4,2,1]
countsort(arr)
print(arr)

