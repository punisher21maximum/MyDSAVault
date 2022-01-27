def func(array):
    '''
    Maximum length subsequence with difference between 
    adjacent elements as either 0 or 1
    '''

    lenOfLongestSubseq = [1 for _ in array]
    hashOfEleSubseqLen = dict()

    for i in range(1, len(array)):

        if abs(array[i] - array[i - 1]) <= 1:
            lenOfLongestSubseq[i] = 1 + lenOfLongestSubseq[i - 1]
        else:
            lenOfLongestSubseq[i] = max(lenOfLongestSubseq[i],
                                        1 + hashOfEleSubseqLen.get(
                                            array[i], 0),
                                        1 + hashOfEleSubseqLen.get(
                                            array[i] + 1, 0),
                                        1 + hashOfEleSubseqLen.get(
                                            array[i] - 1, 0),)

        hashOfEleSubseqLen[array[i]] = lenOfLongestSubseq[i]

    print(max(lenOfLongestSubseq))


def func2(array):
    '''
    Maximum length subsequence with difference between 
    adjacent elements as either 0 or 1
    '''

    lenOfLongestSubseq = [1 for _ in array]
    hashOfEleSubseqLen = dict()

    for i in range(1, len(array)):

        lenOfLongestSubseq[i] = max(lenOfLongestSubseq[i],
                                    1 + max(hashOfEleSubseqLen.get(
                                        array[i], 0),
                                        hashOfEleSubseqLen.get(
                                        array[i] + 1, 0),
                                        hashOfEleSubseqLen.get(
                                        array[i] - 1, 0))
                                    )

        hashOfEleSubseqLen[array[i]] = lenOfLongestSubseq[i]

    print(max(lenOfLongestSubseq))


func([2, 5, 6, 3, 7, 6, 5, 8])
