

def updateResult(longestTravelDist, longestTravelRoutes,
                 currTravelDist, currTravelRoute):
    if currTravelDist > longestTravelDist:
        longestTravelDist = currTravelDist
        longestTravelRoutes = [currTravelRoute]
    elif currTravelDist == longestTravelDist:
        longestTravelRoutes.append([currTravelRoute])

    return (longestTravelDist, longestTravelRoutes)


def method1(maxTravelDist, forwardTravelRoute, reverseTravelRoute):
    longestTravelDist = -1
    longestTravelRoutes = []
    for i in range(len(forwardTravelRoute)):
        forwardTravel = forwardTravelRoute[i]
        for j in range(len(reverseTravelRoute)):
            reverseTravel = reverseTravelRoute[j]
            currTravelDist = forwardTravel[1] + reverseTravel[1]
            currTravelRoute = [forwardTravel[0], reverseTravel[0]]
            if currTravelDist >= longestTravelDist and currTravelDist <= maxTravelDist:
                longestTravelDist, longestTravelRoutes = updateResult(longestTravelDist,
                                                                      longestTravelRoutes,
                                                                      currTravelDist,
                                                                      currTravelRoute)

    print(longestTravelDist, longestTravelRoutes)


def method2(maxTravelDist, forwardTravelRoute, reverseTravelRoute):
    longestTravelDist = -1
    longestTravelRoutes = []

    forwardTravelRoute = sorted(forwardTravelRoute, key=lambda route: route[1])
    reverseTravelRoute = sorted(reverseTravelRoute, key=lambda route: route[1])

    p1 = 0
    p2 = len(reverseTravelRoute) - 1

    while True:
        currTravelDist = forwardTravelRoute[p1][1] + reverseTravelRoute[p2][1]
        currTravelRoute = [forwardTravelRoute[p1]
                           [0], reverseTravelRoute[p2][0]]
        if currTravelDist > maxTravelDist:
            p2 -= 1
        elif currTravelRoute >= longestTravelDist:
            longestTravelDist, longestTravelRoutes = updateResult(longestTravelDist,
                                                                  longestTravelRoutes,
                                                                  currTravelDist,
                                                                  currTravelRoute)

    print(longestTravelDist, longestTravelRoutes)


def mainFunc(maxTravelDist, forwardTravelRoute, reverseTravelRoute):
    '''
    Question:
    For airplane flight, we have two arrays. We have select
    max route length for a plane. Route has 1 value from each
    route array, but sum should be less than maxTravelDist.

    If we find mutiple routes with maxLength that can be travelled 
    return all solutions.

    return id of the route

    Approach:
    For all methods, if 

    Method1 Brute:
    Two forloops, nested. 
    '''
    method1(maxTravelDist, forwardTravelRoute, reverseTravelRoute)
    method2(maxTravelDist, forwardTravelRoute, reverseTravelRoute)


maxTravelDist = 800
forwardTravelRoute = [[1, 300], [2, 450], [3, 700], [4, 500]]
reverseTravelRoute = [[1, 650], [2, 900], [3, 400], [4, 1000], [5, 200]]
mainFunc(maxTravelDist, forwardTravelRoute, reverseTravelRoute)
