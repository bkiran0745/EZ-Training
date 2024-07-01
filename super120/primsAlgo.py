# Prim's Algorithm

vertices = 10
graph = [[0 if i == j else -1 for j in range(vertices)] for i in range(vertices)]

g = {
    1: [(2, 7), (8, 2)],
    2: [(3, 4), (1, 7), (4, 1), (6, 5)],
    3: [(2, 4), (8, 8)],
    4: [(6, 8), (2, 1), (8, 3), (5, 6), (7, 3)],
    5: [(8, 6), (4, 6), (9, 8)],
    6: [(2, 5), (4, 8)],
    7: [(4, 3), (9, 9), (10, 2)],
    8: [(3, 8), (4, 3), (5, 6)],
    9: [(5, 8), (7, 9)],
    10: [(7, 2)]
}

for node, edges in g.items():
    for edge in edges:
        to_node, weight = edge
        graph[node-1][to_node-1] = weight
        graph[to_node-1][node-1] = weight

print("Graph:")
for row in graph:
    print(row)

def prim(graph, start):
    mst = []
    vis = [False] * len(graph)
    max_val = float('inf')
    min_edge = [max_val] * len(graph)
    parent = [-1] * len(graph)
    min_edge[start] = 0

    for _ in range(len(graph)):
        min_weight = max_val
        u = -1
        for v in range(len(graph)):
            if not vis[v] and min_edge[v] < min_weight:
                min_weight = min_edge[v]
                u = v
        
        if u == -1:
            break

        vis[u] = True

        for v in range(len(graph)):
            if graph[u][v] != -1 and not vis[v] and graph[u][v] < min_edge[v]:
                min_edge[v] = graph[u][v]
                parent[v] = u

    for v in range(1, len(graph)):
        if parent[v] != -1:
            mst.append((parent[v] + 1, v + 1, graph[v][parent[v]]))

    return mst

mst = prim(graph, 0)
print("\nMinimum Spanning Tree:", mst)