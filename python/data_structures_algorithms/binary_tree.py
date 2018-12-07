from queue import Queue

class Node:

    def __init__(self, value, level):
        self.value = value
        self.level = level
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root = None):
        self.root = root

    def add(self, value):
        level = 1
        if self.root == None:
            self.root = Node(value, level)
            return
        cur_node = self.root
        while cur_node:

            #Go left
            if value <= cur_node.value:
                if cur_node.left:
                    cur_node = cur_node.left
                    level += 1
                else:
                    cur_node.left = Node(value, level+1)
                    return
            else:
                if cur_node.right:
                    level += 1
                    cur_node = cur_node.right
                else:
                    cur_node.right = Node(value, level+1)
                    return
    
    def level_order(self):
        level = 1
        queue = Queue()
        cur_node = self.root
        while cur_node:
            print('Level {}: {}'.format(cur_node.level,cur_node.value))
            if cur_node.left:
                queue.enqueue(cur_node.left)
            if cur_node.right:
                queue.enqueue(cur_node.right)
            cur_node = queue.dequeue()


    def in_order(self):
        if self.root:
            self.in_order_recur(self.root)

    def in_order_recur(self, node):
        if node.left:
            self.in_order_recur(node.left)
        print('Level {}: {}'.format(node.level, node.value))
        if node.right:
            self.in_order_recur(node.right)

    def pre_order(self):
        if self.root:
            self.pre_order_recur(self.root)

    def pre_order_recur(self, node):
        print('Level {}: {}'.format(node.level, node.value))
        if node.left:
            self.pre_order_recur(node.left)
        if node.right:
            self.pre_order_recur(node.right)

    def post_order(self):
        if self.root:
            self.pre_order_recur(self.root)

    def post_order_recur(self, node):
        if node.left:
            self.post_order_recur(node.left)
        if node.right:
            self.post_order_recur(node.right)
        print('Level {}: {}'.format(node.level, node.value))

if __name__ == '__main__':
    tree = BinaryTree()

    import numpy as np
    np.random.seed(1)
    random_nums = np.random.randint(0,20,size=(20,))
    for each in random_nums:
        tree.add(each)

    print('Level order traversal')
    tree.level_order()

    print('In order traversal')
    tree.in_order()

    print('\nPre order traversal')
    tree.pre_order()

    print('\nPost order traversal')
    tree.post_order()
