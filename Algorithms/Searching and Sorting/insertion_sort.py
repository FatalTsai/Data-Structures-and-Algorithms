def insetionsort(alist):
    for i in range(1, len(alist)):
        index = alist[i]

        j = i-1
        while j >= 0 and index < arr[j]:
            alist[j+1] = arr[j]
            j-= 1
        alist[j+1] = index



arr = [34,55,21,76,83,32,94]
insetionsort(arr)
print(arr)
