from collections import defaultdict


def BFS(graph, V, src):

    queue = [src]
    level = -1

    visited = [False for _ in range(V)]

    while queue:
        level += 1
        for i in range(len(queue)):
            node = queue.pop(0)

            print('level', level, 'node', node)
            visited[node] = True

            adjList = graph[node]
            for adjNode in adjList:
                if not visited[adjNode]:
                    queue.append(adjNode)


if __name__ == '__main__':

    # adjacency graph for tree
    V = 8
    graph = defaultdict(list)

    graph[0].append(1)
    graph[0].append(2)
    graph[1].append(3)
    graph[1].append(4)
    graph[1].append(5)
    graph[2].append(5)
    graph[2].append(6)
    graph[6].append(7)

    # call levels function with source as 0
    BFS(graph, V, 0)
