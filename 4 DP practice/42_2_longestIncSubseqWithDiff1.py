def func(array):
    '''
    Time Complexity: O(n) 
    Auxiliary Space: O(n+n) = O(n)
    '''

    lenOfLongestSubseq = [1 for _ in array]
    hashOfEleSubseqLen = dict()

    for i in range(1, len(array)):

        if abs(array[i] - array[i - 1]) == 1:
            lenOfLongestSubseq[i] = 1 + lenOfLongestSubseq[i - 1]
        else:
            lenOfLongestSubseq[i] = max(lenOfLongestSubseq[i],
                                        1 + hashOfEleSubseqLen.get(
                                            array[i] + 1, 0),
                                        1 + hashOfEleSubseqLen.get(
                                            array[i] - 1, 0),)

        hashOfEleSubseqLen[array[i]] = lenOfLongestSubseq[i]

    print(max(lenOfLongestSubseq))


func([1, 2, 3, 4, 5, 3, 2])
