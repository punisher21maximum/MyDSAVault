def main(arr, K):
    '''

    Approach 1 MergeSort/HeapSort: Time O(NlogN) | Space O(N)
    Sort, then select kth

    Approach 2 QuickSelect: Time Worst O(N^2), Avg O(N)
    In QuickSort
        Partition func:
            Stop when we get pivotIdx as Kth.
        Recur:
            Do not recur both side, only one where we can
            find Kth idx.

    Approach 3 MinHeap: Time O(N + klogN)
    Create minHeap, call extract K times.

    Approach 4 STL library: Time O(n Log n)
    1. insert all eles in set, print kth.
    STL uses a self-balancing BST internally and therefore 
    time complexity of search and insert operations is O(log n) 
    '''
