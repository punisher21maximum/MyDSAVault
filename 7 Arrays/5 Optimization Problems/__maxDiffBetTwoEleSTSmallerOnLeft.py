def main(a):
    '''
    MaxDiff between to eles and smaller appears on left of bigger

    Approach:
    We traverse from right to left, 
    keeping track of max ele found yet.
    If currEle smaller than max then
    we update MaxDiff
    Else we update maxEle
    '''
    minEle = a[0]
    maxDiff = float('-inf')
    for i in range(1, len(a)):
        if a[i] < minEle:
            minEle = a[i]
        else:
            maxDiff = max(maxDiff, a[i] - minEle)

    print(maxDiff)


main([1, 2, 90, 10, 110])
