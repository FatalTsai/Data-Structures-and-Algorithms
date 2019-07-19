def binary_search(list, item):
	first = 0
	last = len(list)- 1
	found = False

	while first <= last and not found:
		midpoint = (first+last)//2
		if list[midpoint] == item:
			found = True
		elif item < list[midpoint]:
			last = midpoint- 1
		else: 
			first = midpoint + 1

	return found

#example
alist = [1, 3, 4, 12, 14, 19, 22, 28, 39, 41]
print(binary_search(alist, 19))
print(binary_search(alist, 27))


