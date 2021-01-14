import sys
sys.stdin = open('input_disjoint.txt','r')

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

for i in range(1,v+1):
    parent[i] = i

for _ in range(e):
    a,b = map(int,input().split())
    if find(parent,a) != find(parent,b):
        union(parent,a,b)
    else:
        break

print(parent)
