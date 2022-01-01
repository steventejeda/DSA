# Overview of LinkedList

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    # Print List method
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
    # Append method
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    # Pop method
    # def pop(self, value):
    #     new_node = Node(value)
    #     if self.length == 0:
    #         return None
    #         temp = self.head
    #         prev = self.head
    #     whg=
        
            
            
    
my_linked_list = LinkedList(4)

my_linked_list.append(6)
my_linked_list.append(10)


my_linked_list.print_list()