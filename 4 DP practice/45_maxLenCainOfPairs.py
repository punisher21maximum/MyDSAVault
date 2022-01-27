class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b


def mainFunc(array):
    '''
    variation of LIS 

    Problem:
    You are given n pairs of numbers. In every pair, the first number is always smaller than 
    the second number. A pair (c, d) can follow another pair (a, b) if b < c

    Approach:
    1. sort the array, by first value in pair 
    2. same as LongestIncSubseq, 
    instead of if prev < curr 
    use if prev[2nd value] < curr[first value]
    '''
    array.sort(key=lambda pair: pair.a)

    lenOfLongestIncSubseq = [1 for num in array]
    idxOfLongestSubseq = 0

    sequences = [None for _ in array]

    for i in range(len(array)):
        currVal = array[i]
        for j in range(i):
            prevVal = array[j]
            if currVal.a > prevVal.b and lenOfLongestIncSubseq[j] + 1 > lenOfLongestIncSubseq[i]:
                lenOfLongestIncSubseq[i] = lenOfLongestIncSubseq[j] + 1
                sequences[i] = j

        if lenOfLongestIncSubseq[i] >= lenOfLongestIncSubseq[idxOfLongestSubseq]:
            idxOfLongestSubseq = i

    print(buildSequence(array, sequences, idxOfLongestSubseq),
          lenOfLongestIncSubseq[idxOfLongestSubseq])


def buildSequence(array, sequences, idx):
    sequence = []

    while idx is not None:
        print(idx)
        sequence.append((array[idx].a, array[idx].b))
        idx = sequences[idx]

    return sequence[::-1]


# Driver program to test above function
arr = [Pair(5, 24), Pair(15, 25),
       Pair(27, 40), Pair(50, 60)]

mainFunc(arr)
