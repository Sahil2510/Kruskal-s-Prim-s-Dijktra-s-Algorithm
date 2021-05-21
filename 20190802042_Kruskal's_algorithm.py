# kruskal's algorithm:

from collections import defaultdict

# Class to represent a graph
print("Kruskal's Algorithm Implementation: ")

class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []  # default dictionary


    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])


    def search(self, parent, i):
        if parent[i] == i:
            return i
        return self.search(parent, parent[i])


    def connection(self, parent, rank, x, y):
        xroot = self.search(parent, x)
        yroot = self.search(parent, y)


        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot

        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # The main function to construct MST using Kruskal's Algorithm
    def Kruskal_Algorithm(self):

        result = []  # This will store the resultant MST
        # An index variable, used for sorted edges
        i = 0
        # An index variable, used for result[]
        e = 0

        self.graph = sorted(self.graph,
                            key=lambda item: item[2])

        parent = []
        rank = []

        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Number of edges to be taken is equal to V-1
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.search(parent, u)
            y = self.search(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.connection(parent, rank, x, y)

        min_root = 0
        print("Edges in the Minimum Spanning Tree: ")
        for u, v, weight in result:
            min_root += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree", min_root)


# Driver code

s = Graph(4)
s.addEdge(0, 1, 10)
s.addEdge(0, 2, 6)
s.addEdge(0, 3, 5)
s.addEdge(1, 3, 15)
s.addEdge(2, 3, 4)

s.Kruskal_Algorithm()
