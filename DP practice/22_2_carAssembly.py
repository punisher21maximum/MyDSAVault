def carAssembly(stationTime, lineSwitchTime, enterTime, exitTime):
    '''
    Given two assembly lines.
    Each has same N number of startions.
    Cost:
        There is cost for:
        - entering line ei
        - leaving line xi
        - statying at a station in line, aij
        - extra cost to switch the line, tij
            from line i to station j
    Find min cost of assembly.
    '''
    numStation = len(stationTime[0])
    T1 = 0
    T2 = 0

    T1 = enterTime[0] + stationTime[0][0]
    T2 = enterTime[1] + stationTime[1][0]

    for i in range(1, numStation):
        T1dash = min(T1 + stationTime[0][i],
                     T2 + lineSwitchTime[1][i] + stationTime[0][i])
        T2dash = min(T2 + stationTime[1][i],
                     T1 + lineSwitchTime[0][i] + stationTime[1][i])

        T1, T2 = T1dash, T2dash

    return min(T1 + exitTime[0],
               T2 + exitTime[1])


# inputs
stationTime = [[4, 5, 3, 2],
               [2, 10, 1, 4]]
lineSwitchTime = [[0, 7, 4, 5],
                  [0, 9, 2, 8]]  # lineSwitchTime[i][j], form line i to station j
enterTime = [10, 12]
exitTime = [18, 7]

print(carAssembly(stationTime, lineSwitchTime, enterTime, exitTime))
