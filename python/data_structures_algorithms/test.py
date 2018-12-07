class Graph:

    def __init__(self, size):
        self.size = size
        self.adj_matrix = [[0 for i in range(size)] for j in range(size)]

    def add_comparison(self, video_1, video_2, value):
        '''
        Args:
        video_1 = id of first video in comparison
        video_2 = id of second video in comparison
        value: 1 if video_one is better, -1 if video_two is better
        '''

        self.adj_matrix[video_1][video_2] = value
        self.adj_matrix[video_2][video_1] = -1 * value

        #update video_one row with all things video_two was bigger than
        for video_3 in range(self.size):

            if video_3 != video_1 and self.adj_matrix[video_2][video_3] == value:
                self.adj_matrix[video_1][video_3] = value
                self.adj_matrix[video_3][video_1] = -1 * value

            if video_3 != video_2 and self.adj_matrix[video_1][video_3] == -1 * value:
                self.adj_matrix[video_2][video_3] = -1 * value
                self.adj_matrix[video_3][video_2] = value



    def find_best(self):
        to_return = []

        is_biggest = True
        for r in range(self.size):
            for c in range(self.size):
                if self.adj_matrix[r][c] < 0:
                    is_biggest = False
            if is_biggest:
                to_return.append(r)
            is_biggest = True
        return to_return

    def __str__(self):
        to_return = ''
        for r in range(self.size):
            for c in range(self.size):
                to_return += str(self.adj_matrix[r][c]) + '\t'
            to_return += '\n'
        return to_return

if __name__ == '__main__':
    graph = Graph(5)
    graph.add_comparison(1,0,1)
    print(str(graph))
    graph.add_comparison(4,1,1)
    print(str(graph))
    graph.add_comparison(3,4,-1)
    graph.add_comparison(2,1,1)
    graph.add_comparison(3,2,1)
    print(str(graph))
    print(graph.find_best())