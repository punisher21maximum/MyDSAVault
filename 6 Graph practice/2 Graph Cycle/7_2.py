from collections import defaultdict


class G:

    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)
        for node in range(self.V):
            self.graph[node] = [float('inf')] * self.V

    def addEdge(self, src, dest, weight):

        self.graph[src][dest] = weight

        # for undirected graph
        # self.graph[dest].append(src)

    def printG(self):

        for i in self.graph:
            print(i, ':', self.graph[i])

    def detectNegativeCycle(self):
        '''
        Approach 1:       
        Keep Two flags: 1. isNegative 2. isCycle 
        if both are true --> negative cycle found 
        flag 1: isNegative: set true if negative edge, set false when done 
        flag 2: isCycle: set true if cycle found 

        Approach 2: Floyd Warshall 
        Distance for a node from itself should be zero,
        if it is not zero, negative cycle.
        '''
        dist = [[0] * self.V for row in range(self.V)]  # copy of graph

        for u in range(self.V):
            for v in range(self.V):
                dist[u][v] = self.graph[u][v]

        for intMedNode in self.graph:  # int = intermediateNode
            for u in self.graph:
                for v in self.graph:
                    dist[u][v] = min(dist[u][v],
                                     dist[u][intMedNode] + dist[intMedNode][v])

        for node in self.graph:
            if dist[node][node] < 0:
                return True
        return False


if __name__ == "__main__":

    g = G(4)

    g.addEdge(0, 0, 0)
    g.addEdge(0, 1, 1)
    g.addEdge(1, 1, 0)
    g.addEdge(1, 2, -1)
    g.addEdge(2, 2, 0)
    g.addEdge(2, 3, -1)
    g.addEdge(3, 0, -1)
    g.addEdge(3, 3, 0)

    g.printG()

    res = g.detectNegativeCycle()
    print(res)
