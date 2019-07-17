class Node:  
    def __init__(self, data):
        self.item = data
        self.ref = None

class LinkedList:  
    def __init__(self):
        self.head = None

    def traverse_list(self):  
        if self.head is None:
            print("List has no element")
            return
        else:
            n = self.head
            while n is not None:
                print(n.item , " ")
                n = n.ref

    def insert_head(self, data):
    	new_node = Node(data)
        new_node.ref = self.head
        self.head= new_node


    def insert_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            n= n.ref
        n.ref = new_node

    def insert_after_item(self, x, data):
        n = self.head
        print(n.ref)
        while n is not None:
            if n.item == x:
                break
            n = n.ref
        if n is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def insert_before_item(self, x, data):
        if self.head is None:
            print("List has no element")
            return

        if x == self.head.item:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return

        n = self.head
        print(n.ref)
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref
        if n.ref is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def insert_at_index (self, index, data):
        if index == 1:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
        i = 1
        n = self.head
        while i < index-1 and n is not None:
            n = n.ref
            i = i+1
        if n is None:
            print("Index out of bound")
        else: 
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def get_count(self):
        if self.head is None:
            return 0;
        n = self.head
        count = 0;
        while n is not None:
            count = count + 1
            n = n.ref
        return count

    def search_item(self, x):
        if self.head is None:
            print("List has no elements")
            return
        n = self.head
        while n is not None:
            if n.item == x:
                print("Item found")
                return True
            n = n.ref
        print("item not found")
        return False

    def make_new_list(self):
        nums = int(input("How many nodes do you want to create: "))
        if nums == 0:
            return
        for i in range(nums):
            value = int(input("Enter the value for the node:"))
            self.insert_at_end(value)

    def delete_head(self):
        if self.headis None:
            print("The list has no element to delete")
            return 
        self.head = self.head.ref

    def delete_tail(self):
        if self.head is None:
            print("The list has no element to delete")
            return

        n = self.head
        while n.ref.ref is not None:
            n = n.ref
        n.ref = None

    def delete_element_by_value(self, x):
        if self.start_node is None:
            print("The list has no element to delete")
            return

        if self.start_node.item == x:
            self.start_node = self.start_node.ref
            return
        
        n = self.start_node
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref

        if n.ref is None:
            print("item not found in the list")
        else:
            n.ref = n.ref.ref


     def reverse_linkedlist(self):
        prev = None
        n = self.head
        while n is not None:
            next = n.ref
            n.ref = prev
            prev = n
            n = next
        self.head = prev














