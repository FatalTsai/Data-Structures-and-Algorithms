class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

def baseconverter(n, b):
	digits = "0123456789ABCDEF"
	stack = Stack()

	while n > 0:
		rem = n % b
		stack.push(rem)
		n = n // b

	string = ""
	while not stack.isEmpty():
		string += digits[stack.pop()]

	return string


n = int(input("Enter the number: "))
b = int(input("Enter the base: "))
print(baseconverter(n, b))


