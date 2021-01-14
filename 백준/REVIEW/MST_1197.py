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

V, E = map(int,input().split())
edges, parent = [], [i for i in range(V+1)]
result = 0
for _ in range(E):
    a, b, c = map(int,input().split())
    edges.append((c,a,b))
edges.sort()
for edge in edges:
    cost, start, end = edge
    if find(parent, start) != find(parent, end):
        union(parent, start, end)
        result += cost
print(result)