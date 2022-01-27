def main(arr):
    '''
    Question: First all neg than pos.

    Approach 1: Modified Partition Process of Quick Sort

    Approach 2: Modified Insertion Sort
    if arr[i-1] > 0 and arr[i] < 0:
        shift rotate

    Approach 3: Time O(n log n) | Space O(N): Optimized Merge Sort 
    Modify merge, first add neg from left and right
    subArray into merged array, then remaining from
    left and right.

    '''
