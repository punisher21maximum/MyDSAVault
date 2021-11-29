'''
1. create G
2. find which is the first letter to be chosen based on second or third letter
'''


class G:

    def __init__(self):
        self.graph = dict()

        self.numToLetter = dict(
            zip(
                list(range(10)), list('ABCDEABCDE')
            )
        )

        self.letterToNum = {
            'A': [0, 5],
            'B': [1, 6],
            'C': [2, 7],
            'D': [3, 8],
            'E': [4, 9]
        }

    def addEdge(self, u, v):

        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)

        self.V = len(self.graph)

    def printG(self):

        for node in self.graph:
            print(node, self.graph[node])

    def findSrc(self, walk):

        numWalk = []

        if walk[0] != walk[1]:
            letter1 = walk[0]
            letter2 = walk[1]
        else:
            letter1 = walk[1]
            letter2 = walk[2]

        numsOfLetter1 = self.letterToNum[letter1]
        numsOfLetter2 = self.letterToNum[letter2]

        for num1 in numsOfLetter1:
            for num2 in numsOfLetter2:
                if num2 in self.graph[num1]:
                    numWalk += [num1, num2]

        if walk[0] == walk[1]:
            letter0 = walk[0]
            numsOfLetter0 = self.letterToNum[letter0]

            if numWalk[0] == numsOfLetter0[0]:
                numOfLetter0 = numsOfLetter0[1]
            else:
                numOfLetter0 = numsOfLetter0[0]

            numWalk.insert(0, numOfLetter0)

        # print(numWalk)
        self.petersonProblem(walk, numWalk, len(numWalk) - 1)

    def petersonProblem(self, walk, numWalk, srcIdx):

        if srcIdx == len(walk) - 1:
            print(numWalk)
            return

        queue = [numWalk[srcIdx]]

        while queue:
            currentNode = queue.pop(0)

            nextLetter = walk[srcIdx + 1]

            letterAdj = False
            adjList = self.graph[currentNode]
            for adjNode in adjList:
                adjLetter = self.numToLetter[adjNode]
                if nextLetter == adjLetter:
                    numWalk += [adjNode]

                    letterAdj == True
                    self.petersonProblem(walk, numWalk, srcIdx + 1)

                    break

            if not letterAdj:
                return 'Not Possible'  # , numWalk, currentNode, nextLetter)

        return numWalk


if __name__ == "__main__":

    g = G()

    # A - A
    g.addEdge(0, 5)
    g.addEdge(1, 6)
    g.addEdge(2, 7)
    g.addEdge(3, 8)
    g.addEdge(4, 9)
    # outer
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
    g.addEdge(4, 0)
    # inner
    g.addEdge(5, 7)
    g.addEdge(6, 8)
    g.addEdge(7, 9)
    g.addEdge(8, 5)
    g.addEdge(9, 6)

    g.printG()

    print(g.findSrc('ABCCAAED'))
