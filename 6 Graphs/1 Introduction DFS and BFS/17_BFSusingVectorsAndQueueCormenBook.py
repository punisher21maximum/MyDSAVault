

class G:

    def __init__(self):
        self.graph = dict()

    def addEdge(self, src, dest):

        if src not in self.graph:
            self.graph[src] = []
        if dest not in self.graph:
            self.graph[dest] = []

        self.graph[src].append(dest)

        # for undirected graph
        self.graph[dest].append(src)

        self.V = len(self.graph)

    def printG(self):

        for i in self.graph:
            print(i, ':', self.graph[i])

    def traverseBFS(self, visited, distances, parent, node):

        queue = [node]

        visited[node] = 'Grey'

        while queue:
            node = queue.pop(0)

            print(node, end=' ')

            adjacencyList = self.graph[node]
            for adjNode in adjacencyList:
                if visited[adjNode] == 'White':
                    visited[adjNode] = 'Grey'
                    distances[adjNode] = distances[node] + 1
                    parent[adjNode] = node

                    queue.append(adjNode)

        visited[node] = 'Black'

    def BFSusingColorsCormenBook(self):
        '''
        White - Non-visited
        Grey - partially visited 
        Black - Visited
        '''
        visited = ['White'] * self.V
        distances = [0] * self.V
        parent = [-1] * self.V

        for node in self.graph:
            if visited[node] == 'White':
                self.traverseBFS(visited, distances, parent, node)

# Code


if __name__ == "__main__":

    g = G()

    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(1, 4)
    g.addEdge(2, 5)
    g.addEdge(2, 6)

    g.printG()

    g.BFSusingColorsCormenBook()
