def tiling(N):

    # 2xN board | 2x1 tile
    if N == 1 or N == 2:
        return N
    return tiling(N-1) + tiling(N-2)


def tilingDPUp(N):

    arr = [1, 2]

    for n in range(2, N+1):
        arr.append(arr[n-1] + arr[n-2])

    return arr[N]
