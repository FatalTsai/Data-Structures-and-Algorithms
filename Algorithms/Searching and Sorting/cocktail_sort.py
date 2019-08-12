# a variation of bubble sort but faster

def cocktailsort(arr):
    n = len(arr)
    swap = True
    start = 0
    end = n-1

    while (swap == True):
        swap = False
        for i in range(start, end): 
            if (arr[i] > arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swap = True
        if (swap == False): 
            break
    
    #reset swap flag
    swap = False 
    end -= 1

    for i in range(end-1, start-1, -1):
        if (arr[i] > arr[i+1]):
            arr[i], arr[i+1]=arr[i+1], arr[i]
            swap=True

    start += 1


arr = [4,-2,3,-4,1,2,5,-3,1,0]
cocktailsort(arr)
print(arr)






