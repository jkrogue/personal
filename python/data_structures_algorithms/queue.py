class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:

    def __init__(self, head=None):
        self.head = None
        self.tail = None
        self.size = 0
        if head != None:
            self.head = head
            self.tail = head
            self.size = 1

    def enqueue(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.head:
            to_return = self.head
            if self.head == self.tail:
                self.tail = None
            self.head = self.head.next
            self.size -= 1
            return to_return.value
        return None

    def is_empty(self):
        return self.size == 0

    def __str__(self):
        to_return = []
        cur_node = self.head
        while cur_node:
            to_return.append(cur_node.value)
            cur_node = cur_node.next
        return str(to_return)

if __name__ == '__main__':
    my_queue = Queue()

    print(my_queue.dequeue())

    my_queue.enqueue(3)
    my_queue.enqueue(2)
    my_queue.enqueue(3.5)    
    my_queue.enqueue(5)
    my_queue.enqueue('apples')
    my_queue.enqueue(1)
    print(my_queue)
    print(my_queue.dequeue())
    print(my_queue.dequeue())
    print(my_queue.dequeue())
    print(my_queue.dequeue())
    print(my_queue.dequeue())
    print(my_queue.dequeue())
    print(my_queue.dequeue())
