from collections import defaultdict


class G:

    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(dict)

    def addEdge(self, u, v, wt):
        '''
        {
            node1:{
                adjNode1: dist11,
                adjNode2: dist12,...
            },
            node2:{
                adjNode1: dist21,
                adjNode2: dist22,...
            },...
        }
        '''

        self.graph[u][v] = wt

        # for undirected graph
        self.graph[v][u] = wt

    def printG(self):

        for node in self.graph:
            adjList = self.graph[node]
            print(node, end=' : ')
            for adjNode in adjList:
                print(adjNode, adjList[adjNode], end=' - ')
            print()

    def printMST(self, parent):

        print('Edge\tWeight')
        print(parent)
        for node, prevNode in enumerate(parent):
            if node != 0:
                wt = self.graph[node][prevNode]
                print(prevNode, '-', node, '\t', wt)

    def getNearestUnvisitedNode(self, distances, visited):

        minDist, minDistNode = float("inf"), None

        for node in range(self.V):
            if not visited[node] and distances[node] <= minDist:
                minDist = distances[node]
                minDistNode = node

        return minDistNode

    def boruvkaMST(self, src=0):
        '''
        Boruvka thoery:
        1) Input is a connected, weighted and un-directed graph.
        2) Initialize all vertices as individual components (or sets).
        3) Initialize MST as empty.
        4) While there are more than one components, do following
        for each component.
            a)  Find the closest weight edge that connects this 
                component to any other component.
            b)  Add this closest edge to MST if not already added.  
        5) Return MST.

        '''

        parent = []
        rank = []

        cheapest = []


if __name__ == "__main__":

    graph = G(9)
    graph.addEdge(0, 1, 4)
    graph.addEdge(0, 7, 8)
    graph.addEdge(1, 2, 8)
    graph.addEdge(1, 7, 11)
    graph.addEdge(2, 3, 7)
    graph.addEdge(2, 8, 2)
    graph.addEdge(2, 5, 4)
    graph.addEdge(3, 4, 9)
    graph.addEdge(3, 5, 14)
    graph.addEdge(4, 5, 10)
    graph.addEdge(5, 6, 2)
    graph.addEdge(6, 7, 1)
    graph.addEdge(6, 8, 6)
    graph.addEdge(7, 8, 7)

    # graph.printG()

    graph.prims(0)
