import math
# import sys
# sys.stdin = open('input_4386.txt','r')

def find(parent,x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent,a,b):
    a = find(parent, a)
    b = find(parent, b)
    if b > a:
        parent[b] = a
    else:
        parent[a] = b

def get_dist(x,y):
    x1,y1,i = x
    x2,y2,j = y
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

N = int(input())
graph, edges, parent = [], [], [i for i in range(N+1)]
for i in range(1,N+1):
    a,b = map(float,input().split())
    graph.append((a,b,i))

for i in range(N):
    for j in range(i+1,N):
        edges.append((get_dist(graph[i], graph[j]),i,j))

# for j in range(2):
#     graph.sort(key=lambda x:x[j])
#     before = graph[0][2]
#     for i in range(1,N):
#         current = graph[i][2]
#         edges.append((get_dist(graph[i],graph[i-1]),before,current))
#         before = current
edges.sort()
answer = 0
for edge in edges:
    cost, x, y = edge
    if find(parent,x) != find(parent,y):
        union(parent,x,y)
        answer += cost
print(format(answer,".2f"))
