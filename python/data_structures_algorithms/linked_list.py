class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self, value = None):
        if value:
            self.head = Node(value)
            self.size = 1
        else:
            self.head = None
            self.size = 0

    def append(self, value):
        if self.head:
            self.get_node(self.size - 1).next = Node(value)
        else:
            self.head = Node(value)
        self.size += 1

    def get_node(self, index):
        LinkedList._check_size(index, self.size)
        cur_node = self.head
        count = 0
        while (cur_node):
            if count == index:
                return cur_node
            count += 1
            cur_node = cur_node.next

    def insert(self, index, value):
        LinkedList._check_size(index, self.size+1)
        new_node = Node(value)
        if index == 0:
            if self.head == None:
                self.head = new_node
            else:
                new_node.next = self.head.next
                self.head = new_node
        else:
            old_node = self.get_node(index - 1)
            new_node.next = old_node.next
            old_node.next = new_node
        self.size += 1

    def remove(self, index):
        LinkedList._check_size(index, self.size)
        if index == 0:
            self.head = self.head.next
        else:
            node = self.get_node(index - 1)
            node.next = node.next.next
        self.size -= 1

    def __getitem__(self, index):
        return self.get_node(index).value

    def __setitem__(self, index, value):
        self.insert(index, value)

    def __delitem__(self, index):
        self.remove(index)

    def __iter__(self):
        self.cur_node = self.head
        return self

    def __next__(self):
        if self.cur_node:
            to_return = self.cur_node.value
            self.cur_node = self.cur_node.next
            return to_return
        else:
            raise StopIteration

    @staticmethod
    def _check_size(index, size):
        if index >= size or index < 0:
            raise IndexError ("Index {} out of bounds in size {} LinkedList".format(index, size))


if __name__ == "__main__":
    my_list = LinkedList()

    print(my_list.size)
    my_list.append('yes')

    my_list.append('no')
    my_list.append('maybe')
    my_list.append('of course')
    my_list.append('love')

    print(my_list.size)
    for each in my_list:
        print(each)

    print ("\n",my_list[2])
    del my_list[2]
    print (my_list[2])    
    for each in my_list:
        print(each)