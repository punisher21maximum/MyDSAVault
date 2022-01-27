def main(arr):
    '''
    Question: Given array with neg and pos, intergers.
    Rearrage as such, alternate neg and pos. Extra
    num at the end. Without maintaining the order of 
    appearance.

    Approach:
    Use quicksort, partition function to seperate neg
    and pos, thats in arr first all neg and then all pos.

    Then place pos at alternate position. 
    '''
