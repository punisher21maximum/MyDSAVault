def partition(a, l, r):
    idx = l

    # pivot is r
    for i in range(l, r):
        if a[i] < a[r]:
            a[i], a[idx] = a[idx], a[i]
            idx += 1

    a[idx], a[r] = a[r], a[idx]

    return idx


def quickSort(a, l, r, k):
    if l > r:
        return
    if l == r:
        if l == k:
            return a[k]
        return

    pi = partition(a, l, r)
    # print(l, r, pi)
    if k == pi:  # opmzn1
        return a[pi]
    elif k < pi:  # opmzn2
        return quickSort(a, l, pi - 1, k)
    else:
        return quickSort(a, pi + 1, r, k)


a = [64, 25, 12, 22, 11, 99]
for k in range(len(a)):
    print(quickSort(a, 0, len(a) - 1, k))
print(a)
