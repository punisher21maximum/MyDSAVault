

class G:

    def __init__(self, V):

        self.V = V
        self.graph = dict()

    def addEdge(self, u, v, w):
        pass

    def isConnected(self):
        pass

    def reverseDeleteMST(self):

        # Non-inc order
        self.graph.sort(key=lambda edge: edge[2], reverse=True)

        MSTweight = 0

        for i in range(len(self.graph)):
            edge = self.graph[i]

            # s1: delete edge
            self.graph.remove(edge)

            # s2: check if graph connected
            connected = self.isConnected()

            # s3: if disconnected, add edge back, add to MST
            if connected:
                self.graph.insert(0, edge)

                w = edge[2]
                MSTweight += w
