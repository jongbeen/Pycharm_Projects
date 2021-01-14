import sys
sys.stdin = open('input_kruskal.txt','r')

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v + 1)
edges, graph = [], []
graph_sum = 0

for i in range(v + 1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()

for edge in edges:
    cost, a, b = edge
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        graph.append((a, b, cost))
        graph_sum += cost
for edge in graph:
    a, b, cost = edge
    print('start:', a, ' end:', b, " cost:", cost)
print(graph_sum)