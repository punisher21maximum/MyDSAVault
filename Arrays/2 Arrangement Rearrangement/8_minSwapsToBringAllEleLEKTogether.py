def main(arr, K):
    '''
    Question: Minimum swaps required to bring all 
    elements less than or equal to k together
    Approach:
    Two pointer + sliding window approach.

    Count the total number of ele LE K, say 'cnt'.
    Now keep p1 and p2 at idx 0, and move p2 till 
    idx cnt-1 and count num of ele GT K, say X.
    Now minimise this X, while sliding the window,
    by moving p1 and p2 by 1 each. if arr[p1-1] > K
    X-=1 and if arr[p2] > K then X+=1.

    Take min of X, that is ans.
    '''
