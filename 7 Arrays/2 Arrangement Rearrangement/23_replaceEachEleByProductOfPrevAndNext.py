def main(arr):
    '''
    Question: Replace each ele by product of it's
    prev and next

    Approach:
    '''
    prev = arr[0]
    for i in range(len(arr)):
        curr = arr[i]

        if i == len(arr) - 1:
            next = arr[i]
        else:
            next = arr[i+1]
        arr[i] = prev * next

        prev = curr

    print(arr)


main([2, 3, 4, 5, 6])
