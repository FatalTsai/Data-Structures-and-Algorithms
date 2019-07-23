def binary_search(alist, item):
	first = 0
	last = len(alist)- 1
	found = False

	while first <= last and not found:
		midpoint = (first+last)//2
		if alist[midpoint] == item:
			found = True
		elif item < alist[midpoint]:
			last = midpoint- 1
		else: 
			first = midpoint + 1

	return found

#example
alist = [1, 3, 4, 12, 14, 19, 22, 28, 39, 41]
print(binary_search(alist, 19))
print(binary_search(alist, 27))

#-------------Recursive Version------------------------------
def BinarySearch(alist, item):
	if len(alist) == 0:
		return False
	else:
		midpoint = len(alist)//2
		if alist[midpoint]== item:
	          return True
	        else:
	          if item< alist[midpoint]:
	            return binarySearch(alist[:midpoint], item)
	          else:
	            return binarySearch(alist[midpoint+1:], item)
