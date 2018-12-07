"""
HashMap is an implementation of a Map (set of keys linked to values with no duplicate keys allowed)
    using a hashtable.  Collisions are handled by storing the key value pairs as a LinkedList
    at the index indicated by the hashcode 
"""

class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return '{}: {}'.format(self.key, self.value)

class HashMap:

    def __init__(self):
        self.table = [None] * 10000
        self.count = 0

    def store(self, key, value):
        hash = self.hash_function(key)
        if self.table[hash]:
            cur_node = self.table[hash]
            while cur_node.key != key and cur_node.next:
                cur_node = cur_node.next
            if cur_node.key == key:
                cur_node.value = value
            else:
                cur_node.next = Node(key, value)
        else:
            self.table[hash] = Node(key, value)


    def lookup(self, key):
        hash = self.hash_function(key)
        if self.table[hash]:
            cur_node = self.table[hash]
            while cur_node.key != key and cur_node.next:
                cur_node = cur_node.next
            if cur_node.key == key:
                return cur_node.value
            else:
                return -1
        else:
            return -1

    def hash_function(self, key):
        hash = ord(key[0]) * 331 + ord(key[1]) * 31
        if len(key) > 2:
            hash *= ord(key[2])
        hash %= 10000
        return hash

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        while self.count < len(self.table) and not self.table[self.count]:
            self.count += 1
        if self.count >= len(self.table):
            raise StopIteration
        else:
            to_return = self.table[self.count]
            self.count += 1
            return to_return


if __name__ == '__main__':
    capitals = HashMap()
    capitals.store('CA', 'Sacramento')
    capitals.store('TX', 'Austin')
    capitals.store('CO', 'Denver')
    capitals.store('UT', 'Provo')
    capitals.store('UT', 'Salt Lake City')

    print("US Capitals")
    for each in capitals:
        print(str(each))

    #should be -1
    print(capitals.lookup('Sacramento'))

    #should be Sacramento
    print(capitals.lookup('CA'))

    #should be -1
    print(capitals.lookup('tx'))

    #should be Austin
    print(capitals.lookup('TX'))
