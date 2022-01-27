import copy


def func(board, p, q):
    """
    Problem - Given a matrix, m*n size. We are given starting positions.
    p - p is col index of row 0,
    q - q is col index of last row.
    We have to find the maxPathSum, starting once from 1st row p col [0, p],
    and go downwards. Then we travel from last row q col [numRows - 1, q]
    and travel upwards.
    """

    maxSum = float("-inf")

    m, n = len(board), len(board[0])
    board2 = copy.deepcopy(board)

    # for r in range(1, m):
    #     for c in range(max(0, p - r), min(n - 1, p + r) + 1):
    #         currMax = float("-inf")
    #         if c >= max(0, p - (r - 1)) and c <= min(n - 1, p + (r - 1)):
    #             currMax = board[r - 1][c]
    #         if c - 1 >= max(0, p - (r - 1)):
    #             print("c-1")
    #             currMax = max(currMax, board[r - 1][c - 1])
    #         if c + 1 <= min(n - 1, p + (r - 1)):
    #             print("c+1")
    #             currMax = max(currMax, board[r - 1][c + 1])

    #         if currMax is not float("-inf"):
    #             board[r][c] += currMax

    #         if r == m - 1:
    #             maxSum = max(maxSum, board[r][c])
    #         print(
    #             ">>>",
    #             r,
    #             c,
    #             p,
    #             max(0, p - (r - 1)),
    #             min(n - 1, p + (r - 1)),
    #             currMax,
    #             board,
    #         )

    print(board)
    board = board2
    print(board)
    ctr = 1
    for r in range(m - 2, -1, -1):
        print("row", r)
        for c in range(max(0, q - ctr), min(n - 1, q + ctr) + 1):
            print("col", c)
            currMax = float("-inf")
            if c >= max(0, p - (ctr - 1)) and c <= min(n - 1, p + (ctr - 1)):
                currMax = board[r - 1][c]
            if c - 1 >= max(0, p - (ctr - 1)):
                print("p-", c - 1)
                currMax = max(currMax, board[r + 1][c - 1])
                print("p+", c + 1)
            if c + 1 <= min(n - 1, p + (ctr - 1)):
                currMax = max(currMax, board[r + 1][c + 1])

            board[r][c] += currMax

            if r == 0:
                maxSum = max(maxSum, board[r][c])
            print(">>>", r, c, currMax, board)
        ctr += 1

    print(board)
    print(maxSum)


func([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 0)
