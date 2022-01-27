

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
        # self.graph[dest].append(src)

    def printG(self):

        for i in self.graph:
            print(i, ':', self.graph[i])

# code

    def topologicalSortOfDirectedSubgraphHelper(self, node, visited,
                                                topologicalOrderOfDirectedSubGraph=[], undirectedEdges=[]):

        visited[node] = True

        # print(node, end=' ')

        adjacencyList = self.graph[node]

        for adjNode in adjacencyList:

            # skipping undirected nodes in topo sort
            adjacencyListOfAdjNode = self.graph[adjNode]
            if node in adjacencyListOfAdjNode:
                if [adjNode, node] not in undirectedEdges:
                    undirectedEdges.append([node, adjNode])
                print('edge', node, '->', adjNode, 'rejected')
                continue

            if not visited[adjNode]:
                print('edge', node, '->', adjNode, 'accepted')
                self.topologicalSortOfDirectedSubgraphHelper(
                    adjNode, visited, topologicalOrderOfDirectedSubGraph, undirectedEdges)

        topologicalOrderOfDirectedSubGraph.insert(0, node)

        return topologicalOrderOfDirectedSubGraph, undirectedEdges

    def topologicalSortOfDirectedSubgraph(self):

        visited = [False] * len(self.graph)
        topologicalOrderOfDirectedSubGraph = []
        undirectedEdges = []

        for node in self.graph:  # range(len(self.graph)):
            if not visited[node]:
                topologicalOrderOfDirectedSubGraph, undirectedEdges = self.topologicalSortOfDirectedSubgraphHelper(
                    node, visited)

        print(topologicalOrderOfDirectedSubGraph, undirectedEdges)
        return topologicalOrderOfDirectedSubGraph, undirectedEdges

    def assignDirectionToEdgesToKeepGAcyclic(self):
        '''
        1. find topological order for subgraph(of only directed graph)
        2. for every undirected edge u<->v if u comes before v in
        topological order, then make it u->v. Else v->u
        '''
        topologicalOrderOfDirectedSubGraph, undirectedEdges = self.topologicalSortOfDirectedSubgraph()

        # changing undirected nodes to directed node
        for fromNode, toNode in undirectedEdges:
            for node in topologicalOrderOfDirectedSubGraph:
                if node == fromNode:
                    self.graph[toNode].remove(fromNode)
                    break
                if node == toNode:
                    self.graph[fromNode].remove(toNode)
                    break


if __name__ == "__main__":

    g = G()
    # g.addEdge(0, 1)
    # g.addEdge(0, 2)
    # g.addEdge(1, 3)
    # g.addEdge(1, 4)
    # g.addEdge(2, 5)
    # g.addEdge(2, 6)
    # g.addEdge(3, 7)
    # g.addEdge(3, 8)
    # g.addEdge(4, 9)
    # g.addEdge(4, 10)

    # directed edges
    g.addEdge(0, 1)
    g.addEdge(0, 5)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(2, 4)
    g.addEdge(3, 4)
    g.addEdge(5, 1)
    g.addEdge(5, 2)
    # undirected edges
    g.addEdge(0, 3)
    g.addEdge(3, 0)
    g.addEdge(0, 2)
    g.addEdge(2, 0)
    g.addEdge(4, 5)
    g.addEdge(5, 4)

    g.printG()

    print()
    g.assignDirectionToEdgesToKeepGAcyclic()

    g.printG()
