def sequenceCount(arr1, arr2, count=0, idx=0):
    if idx == len(arr2):
        return count + 1

    for i in range(len(arr1)):
        # print(i, idx, arr1[i], arr2[idx])
        if arr1[i] == arr2[idx]:
            # print(" hey")
            count = sequenceCount(arr1[i + 1 :], arr2, count, idx + 1)
        if idx == len(arr2):
            return count + 1
    # print(arr1, arr2)
    return count


print(sequenceCount("banana", "ban"))
