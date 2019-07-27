def selectionsort(alist):
   for i in range(len(alist)-1, 0, -1):
       index_max = 0
       for j in range(1, i+1):
           if alist[j]> alist[index_max]:
               index_max = j

       temp = alist[i]
       alist[i] = alist[index_max]
       alist[index_max] = temp

alist = [64,54,26,93,18,8,17,77,55,20,11,7,12,14,19,1,31,44,6]
selectionsort(alist)
print(alist)