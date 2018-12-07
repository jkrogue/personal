
class HashTable:

    def __init__(self):
        self.table = [None] * 1000

    def store(self, string):
        hash = self.hash_function(string)
        self.table[hash] = string

    def lookup(self, string):
        hash = self.hash_function(string)
        if self.table[hash]:
            return hash
        else:
            return -1

    def hash_function(self, string):
        return (ord(string[0]) * 100 + ord(string[1])) % 1000


if __name__ == '__main__':
    table = HashTable()

    table.store("Yes")
    table.store('No')

    #should be 1
    print(table.lookup('Yes'))

    #should be -1
    print(table.lookup('yes'))

    #should be 1
    print(table.lookup('Yesindeedy'))

    #should be 911
    print(table.lookup('No'))