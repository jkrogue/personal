from queue import Queue

class Node:

    def __init__(self, value):
        self.value = value
        self.visited = False
        self.edges = []

class Edge:

    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

class Graph:

    def __init__(self, nodes = [], edges = []):
        self.nodes = nodes
        self.edges = edges

    def insert_edge(self, edge_val, from_val, to_val):
        from_node = None
        to_node = None
        #print('inserting {} from {} to {}'.format(edge_val, from_val, to_val))
        for each in self.nodes:
            #print(each.value)
            if each.value == from_val:
                from_node = each
            elif each.value == to_val:
                to_node = each
        if not from_node:
            from_node = Node(from_val)
            self.nodes.append(from_node)
        if not to_node:
            to_node = Node(to_val)
            self.nodes.append(to_node)
        new_edge = Edge(edge_val, from_node, to_node)
        self.edges.append(new_edge)
        from_node.edges.append(new_edge)
        to_node.edges.append(new_edge)

    def max_index(self):
        max_index = 0
        for each in self.nodes:
            if each.value > max_index:
                max_index = each.value
        return max_index

    def get_node(self, node_val):
        for each in self.nodes:
            if each.value == node_val:
                return each
        return None

    def get_edge_list(self):
        edge_list = []
        for each in self.edges:
            edge_list.append((each.value,each.node_from.value, each.node_to.value))
        return edge_list

    def get_adjacency_list(self):
        '''Return an adjacency list represented as list of tuples where index of list represents value of the node
            and each tuple is (node_to, edge_value)
        '''
        size = self.max_index() + 1
        adjacency_list = [None] * size
        for each in self.edges:
            if adjacency_list[each.node_from.value]:
                adjacency_list[each.node_from.value].append((each.node_to.value, each.value))
            else:
                adjacency_list[each.node_from.value] = [(each.node_to.value, each.value)]
        return adjacency_list

    def get_adjacency_matrix(self):
        '''Return adjacency matrix where index of row is node_from and index of column is node_to and value at
            those indeces represents length of edge
        '''
        size = self.max_index() + 1
        matrix = [[0 for each in range(size)] for each in range(size)]
        for each in self.edges:
            row = each.node_from.value
            col = each.node_to.value
            matrix[row][col] = each.value
        return matrix

    def bfs(self, start_val):
        node = self.get_node(start_val)
        if node == None:
            return None

        to_return = []

        queue = Queue()
        queue.enqueue(node)
        node.visited = True
        while not queue.is_empty():
            node = queue.dequeue()
            to_return.append(node.value)
            edges_out = [each for each in node.edges if each.node_to.value != node.value]
            for each in edges_out:
                node_to = each.node_to
                if not node_to.visited:
                    node_to.visited =True
                    queue.enqueue(node_to)
        return to_return

    def dfs_recur(self, start_val):
        node = self.get_node(start_val)
        if node == Node:
            return None

        return self.dfs_recur_helper(node)

    def dfs_recur_helper(self, node):
        to_return = [node.value]
        edges_out = [each for each in node.edges if each.node_to.value != node.value]
        to_return = []

        stack = []
        stack.push(node)
        node.visited = True
        while len(stack) > 0:
            node = stack.pop()


    def _clear_visited(self):
        for each in self.nodes:
            each.visited = False



if __name__ == '__main__':
    graph = Graph()
    graph.insert_edge(100, 1, 2)
    graph.insert_edge(101, 1, 3)
    graph.insert_edge(102, 1, 4)
    graph.insert_edge(103, 3, 4)

    # Should be [(100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)]
    print (graph.get_edge_list())

    # Should be [None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None]
    print (graph.get_adjacency_list())

    # Should be [[0, 0, 0, 0, 0], [0, 0, 100, 101, 102], [0, 0, 0, 0, 0], [0, 0, 0, 0, 103], [0, 0, 0, 0, 0]]
    print (graph.get_adjacency_matrix())

    graph.insert_edge(103, 1, 5)
    graph.insert_edge(103, 5, 7)

    print('BFS search: \n{}'.format(graph.bfs(1)))
