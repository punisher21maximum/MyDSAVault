'''
For UG:
1. Connected G
2. No Cycle

check is connected?
    if BFS from any random node, reach all nodes -> connected 
check cycle:
    for a node u, if its adjNode v, 
    already visited and not parent of u --> cycle
'''
