def main(arr):
    """
    Question: Given an array of numbers, arrange
    them in a way that yields the largest value.
    For example, if the given numbers are {54, 546, 548, 60},
    the arrangement 6054854654 gives the largest value.
    And if the given numbers are {1, 34, 3, 98, 9, 76, 45, 4},
    then the arrangement 998764543431 gives the largest value.

    Approach:
    sort the array in dec order, to find the bigger
    of two eles, we use this approach.

    A compare func, input n1 and n2, we compare these
    nums for first min(len(n1), len(n2)) digits.

    def compare(n1, n2):

        bigger = None
        for i in range(min(len(n1), len(n2))):
            if n1[i] > n2[i]:
                return n1
            elif n1[i] < n2[i]:
                return n2
        return num with smaller len

    """
    pass


def reverseNum(N):

    revN = 0

    while N:
        revN = revN * 10 + (N % 10)

        N //= 10

    print(revN)


reverseNum(1234)
