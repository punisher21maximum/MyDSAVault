
class Graph:
    '''
    Graph using dict 
    keys: nodes
    values: set of adj nodes
    1 {2, 4}
    4 {1, 3, 5}
    2 {1, 3}
    3 {2, 4, 5}
    5 {3, 4}
    '''

    def __init__(self):
        self.graph = {}

    def addEdge(self, u, v):

        if u not in self.graph:
            self.graph[u] = set()

        if v not in self.graph:
            self.graph[v] = set()

        # add edge u->v
        self.graph[u].add(v)

        # add edge v->u
        self.graph[v].add(u)

    def printG(self):

        for node in self.graph:
            print(node, self.graph[node])


if __name__ == '__main__':

    g = Graph()

    g.addEdge(1, 4)
    g.addEdge(1, 2)
    g.addEdge(2, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 2)
    g.addEdge(3, 4)
    g.addEdge(3, 5)
    g.addEdge(4, 1)
    g.addEdge(4, 3)
    g.addEdge(4, 5)
    g.addEdge(5, 3)
    g.addEdge(5, 4)

    g.printG()
