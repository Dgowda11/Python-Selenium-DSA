from email.errors import NonPrintableDefect


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self,value):
        new_node  = Node(value)
        self.first = new_node
        self.last = new_node
        self.length  = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # Add the Element from the other end of the List for O(1)
    def enqueue(self,value):
        new_node = Node(value)
        if self.length is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    # Add the Element from the Beginning of tbe List for Better O(1)
    def dequeue(self):
        if self.length is None:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1

myQueue = Queue(4)
myQueue.print_queue()
print("Enqueue starts here")
myQueue.enqueue(8)
myQueue.print_queue()
print("Dequeue starts here")
myQueue.dequeue()
myQueue.print_queue()
