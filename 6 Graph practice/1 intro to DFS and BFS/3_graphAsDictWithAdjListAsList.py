
class Graph:
    '''
    Keys: Nodes 
    Values: AdjList
    '''

    def __init__(self, N):
        self.N = N
        self.graph = dict()

    def addEdge(self, u, v):

        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)

        # if UG
        self.graph[v].append(u)

    def printG(self):

        for node, adjList in self.graph.items():
            print(node, ': ', adjList)


if __name__ == "__main__":
    # {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

    graph = Graph(4)
    graph.addEdge(0, 1)
    graph.addEdge(0, 4)
    graph.addEdge(1, 2)
    graph.addEdge(1, 3)
    graph.addEdge(1, 4)
    graph.addEdge(2, 3)
    graph.addEdge(3, 4)

    graph.printG()
