def checkLoopInArray(array):
    """
    Promt:
        Given an array, with +ve or -ve values
        Move in array,
            if value is positive, new position = (i+arr[i])%n
            if value is negative, new position = (i-arr[i])%n

    Approach1: for loop the array n times until we find cycle

    Approach2: create a graph, detect cycle
    when creating graph, don't add self loops
    """
    visited = [False] * len(array)

    position = 0
    visited[0] = True
    for _ in range(len(array)):
        nextPosition = (position + array[position]) % len(array)
        print(nextPosition, position)

        if visited[nextPosition]:
            print("Cycle")
            return

        position = nextPosition
        visited[position] = True

    print("No cycle")


arr = [2, -1, 1, 2, 2]
checkLoopInArray(arr)
