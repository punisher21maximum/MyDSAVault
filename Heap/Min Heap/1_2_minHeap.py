from heapq import heappush, heappop, heapify


class MinHeap:

    def __init__(self):
        self.heap = []

    def getParent(self, i):
        '''
        return parent idx
        '''
        lastIdx = len(self.heap) - 1
        parentIdx = (i-1)//2
        return parentIdx if i <= lastIdx else None

    def getChildren(self, i):
        '''
        return parent idx
        '''
        lastIdx = len(self.heap) - 1
        leftChild, rightChild = None, None

        if i*2 + 1 <= lastIdx:
            leftChild = i*2 + 1
        if i*2 + 2 <= lastIdx:
            rightChild = i*2 + 2

        return (leftChild, rightChild)

    def buildHeap(self, arr):
        lastIdx = len(arr) - 1
        firstParentIdx = (lastIdx - 1) // 2

        for currIdx in reversed(range(firstParentIdx+1)):
            self.siftDown(currIdx)

        return arr

    def siftDown(self, ci):

        lci, rci = self.getChildren(ci)

        mi = None
        while lci:
            rci = float('inf') if rci is None else rci

            if self.h[lci] <= self.h[rci]:
                mi = lci
            else:
                mi = rci

            if self.heap[ci] > self.heap[mi]:
                self.swapVals(self.h, ci, mi)
                ci = mi
            else:
                break

    def siftUp(self, ci):

        if ci is None:
            return

        pi = self.getParent(ci)

        if self.h[ci] < self.h[pi]:
            self.swapVal(self.h, ci, pi)
            ci = pi
            self.siftUp(ci)

    def getMin(self):
        return self.h[0]

    def extractMin(self):
        minVal = self.heap[0]

        self.swap(self.h, 0, len(self.h) - 1)
        self.siftDown(0)

        return minVal

    def insertEle(self, val):
        self.heap.append(val)
        self.siftUp(-1)

    def deleteByIdx(self, ci):
        delVal = self.h[ci]

        while ci != 0 and self.h[self.getParent(ci)] > self.h[ci]:
            self.swap(self.h, ci, self.getParent(ci))
