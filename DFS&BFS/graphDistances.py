#You have a strongly connected directed graph that has positive weights in the adjacency matrix g. The graph is represented as a square matrix, where g[i][j] is the weight of the edge (i, j), or -1 if there is no such edge.

#Given g and the index of a start vertex s, find the minimal distances between the start vertex s and each of the vertices of the graph.

def solution(g, s):
    N = len(g)
    for x in range(N):
        for y in range(N):
            if g[x][y] == -1:
                g[x][y] = float('inf')

    for k in range(N):
        for i in range(N):
            for j in range(N):
                g[i][j] = min(g[i][j], g[i][k] + g[k][j])

    g[s][s] = 0 # distance to self is 0
    return g[s][:]
