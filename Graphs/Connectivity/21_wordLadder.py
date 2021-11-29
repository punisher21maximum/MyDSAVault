from collections import defaultdict


class Graph:

    def __init__(self, V):

        self.graph = defaultdict(list)

    def addEdge(self, u, v):

        self.graph[u].append(v)

        # UG
        self.graph[v].append(v)

        self.V = len(self.graph)

    def printG(self):

        for word in self.graph:
            print(word, self.graph[word])

    def createGraph(self, start, givenDict):

        givenDict[start] = True

        for word in givenDict:
            for otherWord in givenDict:
                if word != otherWord and self.isAdjWord(word, otherWord):
                    self.addEdge(word, otherWord)

    def isAdjWord(self, word, otherWord):

        lenn = len(word)
        numOfSameLetters = 0

        for i in range(lenn):
            if word[i] == otherWord[i]:
                numOfSameLetters += 1

        return lenn - 1 == numOfSameLetters

    def wordLadder(self, srcNode, target):

        visited = {}
        visited[srcNode] = True
        order = []

        if self.wordLadderHelper(srcNode, target, visited, order):
            print('Yes')
        else:
            print('No')

    def wordLadderHelper(self, srcNode, target, visited, path):

        if srcNode == target:
            print('Found', path)
            return True

        adjList = self.graph[srcNode]
        for adjNode in adjList:

            if adjNode in visited or srcNode == adjNode:
                continue

            visited[adjNode] = True
            path.append(adjNode)

            if adjNode == target:
                print('Found, Node: ', [start] + path)
                return True

            self.wordLadderHelper(adjNode, target, visited, path)

            visited[adjNode] = False
            path.pop()

        return False


if __name__ == '__main__':

    g = Graph(V=9)

    givenDict = {
        'poon': True,
        'plee': True,
        'same': True,
        'poie': True,
        'plie': True,
        'poin': True,
        'plea': True
    }

    start = 'toon'
    target = 'plea'

    g.createGraph(start, givenDict)

    g.printG()

    g.wordLadder(start, target)
