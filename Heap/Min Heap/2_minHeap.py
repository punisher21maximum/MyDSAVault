

class MinHeap:

    def __init__(self, array):

        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        lastIdx = len(array) - 1
        firstParentIndex = (lastIdx - 1) // 2

        for currIndex in reversed(range(firstParentIndex + 1)):
            self.siftDown(currIndex, array)

        return array

    def siftDown(self, currentIdx, heap):
        '''
        childOne: heap[(2 * i) + 1]
        childTwo: heap[(2 * i) + 2]
        '''
        childOneIdx = (2 * currentIdx) + 1
        childTwoIdx = (2 * currentIdx) + 2

        childOneIdx = childOneIdx if childOneIdx < len(heap) else None
        childTwoIdx = childTwoIdx if childTwoIdx < len(heap) else None

        minValueChildIdx = None
        if childOneIdx and childTwoIdx:
            if heap[childOneIdx] < heap[childTwoIdx]:
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

        if heap[minValueChildIdx] < heap[currentIdx]:
            self.swap(minValueChildIdx, currentIdx, heap)
            self.siftDown(minValueChildIdx, heap)
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
            self.swap(parentIdx, currentIdx, self.heap)
            self.siftUp(parentIdx)

    def peek(self):

        return self.heap[0]

    def removeMin(self):

        self.swap(0, len(self.heap) - 1, self.heap)
        minNode = self.heap.pop()
        self.siftDown(0, self.heap)
        return minNode

    def insert(self, value):

        self.heap.append(value)
        self.siftUp(len(self.heap)-1)

    def swap(self, idx1, idx2, heap):

        heap[idx1], heap[idx2] = heap[idx2], heap[idx1]


if __name__ == "__main__":

    array = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]

    minheap = MinHeap(array)

    print(minheap.heap)

    # minheap.printLevelOrder()

    print(minheap.removeMin())
    print(minheap.heap)
