class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.height  = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # Push method to add new node to stack
    def push_stack(self,value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    # Pop method to remove the element from the Stack
    def pop_stack(self):
        if self.height == 0:
            return False
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp

# Create the Stack
my_stack = Stack(4)
my_stack.print_stack()

print("Push stack with the new value")
my_stack.push_stack(2)
my_stack.print_stack()

print("pop method to remove the top value")
my_stack.pop_stack()
my_stack.print_stack()

