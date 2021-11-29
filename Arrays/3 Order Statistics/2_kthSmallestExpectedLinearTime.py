'''
Approach 2 QuickSelect: Time Worst O(N^2), Avg O(N)
    In QuickSort
        Partition func:
            Stop when we get pivotIdx as Kth.
        Recur:
            Do not recur both side, only one where we can
            find Kth idx
'''
