class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:

    def __init__(self, head=None):
        self.head = None
        if head != None:
            self.head = Node(head)

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        old_head = self.head
        if old_head:
            self.head = old_head.next
            return old_head.value
        return None

    def peek(self):
        if self.head:
            return self.head.value
        return None

    def __str__(self):
        values = []
        cur_node = self.head
        while cur_node:
            values.append(cur_node.value)
            cur_node = cur_node.next
        return str(values)

if __name__ == '__main__':
    my_stack = Stack()

    print(my_stack.pop())

    my_stack.push(3)
    my_stack.push(2)
    my_stack.push(3.5)    
    my_stack.push(5)
    my_stack.push('apples')
    my_stack.push(1)
    print(my_stack)
    print(my_stack.pop())
    print(my_stack.pop())
    print(my_stack.pop())
    print(my_stack.pop())
    print(my_stack.pop())
