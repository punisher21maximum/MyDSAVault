
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Graph:
    '''
    [0, 1, 2]
    0 -> 1 -> 4 -> /
    1 -> 0 -> 4 -> 2 -> 3 -> /
    2 -> 1 -> 3 -> /    
    '''

    def __init__(self, N):
        self.N = N
        self.graph = [None] * N

    def addEdge(self, u, v):

        # add u->v
        node = Node(v)
        node.next = self.graph[u]
        self.graph[u] = node

        # add v->u, if UG (undirected graph)
        node = Node(u)
        node.next = self.graph[v]
        self.graph[v] = node

    def printG(self):

        for idx in range(self.N):
            print(idx + 1, end=': ')
            node = self.graph[idx]
            while node:
                print(node.value, end=' ')
                node = node.next
            print()


if __name__ == "__main__":
    V = 6
    graph = Graph(V)
    graph.addEdge(5, 1)
    graph.addEdge(5, 4)
    graph.addEdge(1, 2)
    graph.addEdge(1, 3)
    graph.addEdge(1, 4)
    graph.addEdge(2, 3)
    graph.addEdge(3, 4)

    graph.printG()
