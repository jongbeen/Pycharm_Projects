import sys
sys.stdin = open('input_1922.txt','r')

def find(parent,x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]
def union(parent, a, b):
    a = find(parent,a)
    b = find(parent,b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

N = int(input())
M = int(input())
parent, edges, answer = [], [], 0
parent = [0]*(N+1)
for i in range(N+1):
    parent[i] = i
for _ in range(M):
    a,b,c = map(int,input().split())
    edges.append((c,a,b))
edges.sort()

for edge in edges:
    cost, start, end = edge
    if find(parent,start) != find(parent,end):
        union(parent,start,end)
        answer += cost
print(answer)
