#Prim's Algorithm

import sys  # Library for maximum Integer

print("Prim's Algorithm Implementation:")
class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

        # A utility function to print the constructed MST stored in a[]

    def print_MinSpanning(self, a):
        print("Edge \tWeight of tree")
        for i in range(1, self.V):
            print(a[i], "-", i, "\t", self.graph[i][a[i]])

            # A utility function to find the vertex with


    def minKey(self, key, min_span_tree_set):

        # Initilaize min value
        min = sys.maxsize

        for v in range(self.V):
            if key[v] < min and min_span_tree_set[v] == False:
                min = key[v]
                min_index = v

        return min_index

        # Function to construct and print MST for a graph

    # represented using adjacency matrix representation
    def prims_algorithm(self):


        key = [sys.maxsize] * self.V
        a = [None] * self.V  # Array to store constructed MST

        key[0] = 0
        min_span_tree_set = [False] * self.V

        a[0] = -1  # First node is always the root of

        for cout in range(self.V):


            u = self.minKey(key, min_span_tree_set)


            min_span_tree_set[u] = True


            for v in range(self.V):


                if self.graph[u][v] > 0 and min_span_tree_set[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    a[v] = u

        self.print_MinSpanning(a)


t = Graph(5)
t.graph = [[0, 2, 0, 6, 0],
           [2, 0, 3, 8, 5],
           [0, 3, 0, 0, 7],
           [6, 8, 0, 0, 9],
           [0, 5, 7, 9, 0]]

t.prims_algorithm()