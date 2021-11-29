

class MinHeap:

    def __init__(self):

        self.heap = []

    def buildHeap(self, array):
        lastIdx = len(array) - 1
        firstParentIndex = (lastIdx - 1) // 2
        for currIndex in reversed(range(firstParentIndex + 1)):
            print(currIndex)
            self.siftDown(currIndex)
        return array

    def siftDown(self, currentIdx):
        '''
        childOne: heap[(2 * i) + 1]
        childTwo: heap[(2 * i) + 2]
        '''
        childOneIdx = (2 * currentIdx) + 1
        childTwoIdx = (2 * currentIdx) + 2

        childOneIdx = childOneIdx if childOneIdx < len(self.heap) else None
        childTwoIdx = childTwoIdx if childTwoIdx < len(self.heap) else None

        minValueChildIdx = None
        if childOneIdx and childTwoIdx:
            if self.heap[childOneIdx] < self.heap[childTwoIdx]:
                minValueChildIdx = childOneIdx
            else:
                minValueChildIdx = childTwoIdx
        elif childOneIdx and not childTwoIdx:
            minValueChildIdx = childOneIdx
        elif not childOneIdx and childTwoIdx:
            minValueChildIdx = childTwoIdx
        else:
            # no child
            return

        if self.heap[minValueChildIdx] < self.heap[currentIdx]:
            self.swap(minValueChildIdx, currentIdx)
            self.siftDown(minValueChildIdx)
        else:
            # currentIdx has smallest value
            return

    def siftUp(self, currentIdx):
        '''
        parentIdx: (currentIdx - 1) // 2
        '''
        parentIdx = (currentIdx - 1) // 2
        parent = self.heap[parentIdx]

        child = self.heap[currentIdx]

        if currentIdx > 0 and parent > child:
            self.swap(parentIdx, currentIdx)
            self.siftUp(parentIdx)

    def peek(self):

        return self.heap[0]

    def removeMin(self):

        self.swap(0, len(self.heap) - 1)
        minNode = self.heap.pop()
        self.siftDown(0)
        return minNode

    def insert(self, value):

        self.heap.append(value)
        self.siftUp(len(self.heap)-1)

    def swap(self, idx1, idx2):

        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

    def printLevelOrder(self, idx=0):

        if idx < len(self.heap):
            print(self.heap[idx])

            self.printLevelOrder(idx*2+1)
            self.printLevelOrder(idx*2+2)


array = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]

minheap = MinHeap()

for e in array:
    minheap.insert(e)

print(minheap.heap)

minheap.printLevelOrder()
