def mainFunc(arr, d, n):
    '''
    For multiple quick rotations, we store
    arr in tempArr of size 2*n twice.

    startIdx = d % n 
    endIdx = (startIdx + n) % n

    For right rotation:
    startIdx = (n - d) % n 
    endIdx = (startIdx + n) % n
    '''
    print('left', d % n, d % n + n)
    print('left', (n - d) % n, (n - d) % n + n)


arr = [1, 3, 5, 7, 9]
mainFunc(arr, d=2, n=10)
