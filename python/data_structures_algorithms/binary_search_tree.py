from queue import Queue

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root = None):
        self.root = root

    def add(self, value):
        if self.root == None:
            self.root = Node(value)
            return
        cur_node = self.root
        while cur_node:

            #Go left
            if value == cur_node.value:
                return
            elif value < cur_node.value:
                if cur_node.left:
                    cur_node = cur_node.left
                else:
                    cur_node.left = Node(value)
                    return
            else:
                if cur_node.right:
                    cur_node = cur_node.right
                else:
                    cur_node.right = Node(value)
                    return
    
    def delete(self, value):
        cur_node = self.root
        self.root = self.delete_node(self.root, value)

    def delete_node(self, node, value):
        if node == None:
            return None

        # go left
        if value < node.value:
            node.left = self.delete_node(node.left, value)

        # go right
        elif value > node.value:
            node.right = self.delete_node(node.right, value)

        # this is the node to delete
        else:

            #if just has one child then put it in its place
            if node.left == None:
                node = node.right
                return node
            elif node.right == None:
                node = node.left
                return node

            #if has two children, then replace with smallest node above it
            min_value = self.min_value(node.right)
            node.value = min_value
            node.right = self.delete_node(node.right, min_value)
        return node

    def min_value(self, node):
        if node == None:
            return None
        while node.left:
            node = node.left
        return node.value 

    def search(self, value):
        cur_node = self.root
        while cur_node:
            if cur_node.value == value:
                return True
            if value < cur_node.value:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right
        return False

    def level_order(self):
        queue = Queue()
        cur_node = self.root
        while cur_node:
            print(cur_node.value)
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
        print(node.value)
        if node.right:
            self.in_order_recur(node.right)

    def pre_order(self):
        if self.root:
            self.pre_order_recur(self.root)

    def pre_order_recur(self, node):
        print(node.value)
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
        print(node.value)

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

    print(tree.search(5))
    print(tree.search(22))

    tree.delete(5)
    tree.delete(11)
    tree.delete(6)
    tree.delete(22)
    tree.delete(9)
    print('\nIn order after deleting 5, 6, 9, 11')
    tree.in_order()

    for each in random_nums:
        tree.delete(each)

    print('\nIn order after deleting all numbers')
    tree.in_order()
