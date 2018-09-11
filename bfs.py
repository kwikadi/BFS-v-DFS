from collections import defaultdict

# This class represents a directed graph
# using adjacency list representation
class Graph:

    # Constructor
    def __init__(self, count):

        # default dictionary to store graph
        self.graph = defaultdict(list)
        self.count = count

    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)

    # Function to print a BFS of graph
    def BFS(self, s, g):

        # Mark all the vertices as not visited
        visited = [False] * self.count

        # Create a queue for BFS
        queue = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:

            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print (s, end = " ")

            if s == g:
                print("Goal found.")
                return 0

            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

        print("Search failed.")
        return 0

# Driver code

with open('input.txt', 'rb') as inputFile:
    count = int(inputFile.readline())
    a = int(inputFile.readline())
    b = int(inputFile.readline())

    # Create a graph given in
    # the above diagram
    g = Graph(count)
    for i in inputFile.readlines():
        g.addEdge(int(i.split()[0]), int(i.split()[1]))

g.BFS(a,b)
