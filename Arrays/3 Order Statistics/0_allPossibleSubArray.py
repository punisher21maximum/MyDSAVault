arr = [1, 2, 3, 4]

n = len(arr)
for endIdx in range(n+1):
    for startIdx in range(endIdx):
        print(startIdx, endIdx, arr[startIdx: endIdx])
