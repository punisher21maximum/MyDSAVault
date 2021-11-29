from collections import defaultdict


class G:

    def __init__(self, V):
        self.V = V

    def printG(self):

        print(self.graph)

    def printPath(self, src, parent):

        for node in range(self.V):
            currNode = node
            path = [node]
            while parent[node] != -1:
                path.append(parent[node])
                node = parent[node]
            print(currNode, ':', path[::-1])

    def getNearestUnvisitedNode(self, distances, visited):

        minDist, minDistNode = float("inf"), None

        for node in range(self.V):
            if not visited[node] and distances[node] <= minDist:
                minDist = distances[node]
                minDistNode = node

        return minDistNode

    def djiktras(self, src=0):
        '''
        Approach:
        Maintain two sets, mstSet and remainingVertices
        mstSet: has vertices added to MST
        remainingVertices: initially contains all the vertices

        mstSet: nodes are added to mstSet 
        remainingVertices: removed from remainingVertices 
        '''
        visited = [False] * self.V
        distances = [float('inf')] * self.V  # dist from MST of other vertices

        distances[src] = 0

        # path
        parent = [None] * self.V
        parent[src] = -1

        for _ in range(self.V):  # V : to add N vertices

            # find nearest node
            node = self.getNearestUnvisitedNode(
                distances, visited)

            # mark visited
            visited[node] = True

            # updated distances of unvisited adj nodes of node
            for adjNode in range(self.V):
                if self.graph[node][adjNode] > 0 and not visited[adjNode] and \
                        distances[adjNode] > (distances[node] + self.graph[node][adjNode]):
                    distances[adjNode] = distances[node] + \
                        self.graph[node][adjNode]
                    parent[adjNode] = node

        self.printPath(src, parent)


if __name__ == "__main__":

    g = G(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]
               ]

    # graph.printG()

    g.djiktras(0)
