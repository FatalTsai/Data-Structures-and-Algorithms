def partition(arr, low, high):
	i= low-1
	pivot= arr[high]

	for j in range(low, high):
		if arr[j] <= pivot:
			i+= 1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i+1], arr[high] = arr[high], arr[i+1]
	return (i+1)

def quicksort(arr, low, high):
	if low < high:
		p= partition(arr, low, high)
		quicksort(arr, low, p-1)
		quicksort(arr, low+1, high)

alist = [54,69,26,93,17,77,31,44,55,20]
n = len(alist)
quicksort(alist, 0, n-1)
print(alist)
