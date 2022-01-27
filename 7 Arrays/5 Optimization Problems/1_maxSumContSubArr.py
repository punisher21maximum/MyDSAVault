def main(a):
    '''


    '''
    currMax = a[0]
    maxSum = a[0]

    for i in range(1, len(a)):
        currMax = max(a[i], a[i] + currMax)
        maxSum = max(maxSum, currMax)

    print(maxSum)


main([-2, -3, 4, -1, -2, 1, 5, -3])
main()
