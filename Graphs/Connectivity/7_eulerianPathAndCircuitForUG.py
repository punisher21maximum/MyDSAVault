from collections import defaultdict


class G:

    def __init__(self, V):

        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, u, v):

        self.graph[u].append(v)

        # UG
        self.graph[v].append(u)

    def isVertexConnected(self, vertex):

        visited = [False] * self.V
        numVisited = 0

        queue = [vertex]

        while queue:
            node = queue.pop()

            if visited[node]:
                continue
            visited[node] = True
            numVisited += 1

            adjList = self.graph[node]
            for adjNode in adjList:
                queue.append(adjNode)

        return numVisited == self.V

    def isEulerianPathOrCircuit(self):
        '''
        Eulerian Circuit:
        1. all non-zero degree vertices should be connected
        2. all vertices even degree

        Eulerian Path:
        1. all non-zero degree vertices should be connected
        2. 0 or 2 vertices with odd degree,
           other vertices with even degree
        '''

        numOfOddDegreeVertices = 0

        for node in self.graph:
            adjList = self.graph[node]
            if len(adjList) != 0:  # non-zero degree vertex
                if self.isVertexConnected(node) == False:
                    print('Non-zero degree vertex not connected')
                    return False

            numOfOddDegreeVertices += (len(adjList) % 2)

        if numOfOddDegreeVertices == 0:
            print('Eulerian Circuit')
        elif numOfOddDegreeVertices == 2:
            print('Eulerian Path')
        else:
            print('numOfOddDegreeVertices', numOfOddDegreeVertices)


if __name__ == '__main__':

    g1 = G(5)
    g1.addEdge(1, 0)
    g1.addEdge(0, 2)
    g1.addEdge(2, 1)
    g1.addEdge(0, 3)
    g1.addEdge(3, 4)
    g1.isEulerianPathOrCircuit()

    g2 = G(5)
    g2.addEdge(1, 0)
    g2.addEdge(0, 2)
    g2.addEdge(2, 1)
    g2.addEdge(0, 3)
    g2.addEdge(3, 4)
    g2.addEdge(4, 0)
    g2.isEulerianPathOrCircuit()

    g3 = G(5)
    g3.addEdge(1, 0)
    g3.addEdge(0, 2)
    g3.addEdge(2, 1)
    g3.addEdge(0, 3)
    g3.addEdge(3, 4)
    g3.addEdge(1, 3)
    g3.isEulerianPathOrCircuit()

    g4 = G(3)
    g4.addEdge(0, 1)
    g4.addEdge(1, 2)
    g4.addEdge(2, 0)
    g4.isEulerianPathOrCircuit()

    g5 = G(3)
    g5.isEulerianPathOrCircuit()

    # g.isEulerianPathOrCircuit()
