import sys
sys.stdin = open('input_1922.txt', 'r')

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if b > a:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())
M = int(input())
answer= 0
edges, parent = [], [0] * (N + 1)
for i in range(1, N + 1):
    parent[i] = i

for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()
for edge in edges:
    cost, a, b = edge
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        answer += cost
print(answer)
