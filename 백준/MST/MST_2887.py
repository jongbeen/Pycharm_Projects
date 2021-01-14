import sys
sys.stdin = open('input_2887.txt','r')

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
loc, edges,parent = [], [], [0]* (N + 1)
result = 0
for i in range(1,N+1):
    parent[i] = i

for i in range(1,N+1):
    x,y,z = map(int,input().split())
    loc.append([x,y,z,i])

# for i in range(1,N+1):
#     for j in range(i+1,N+1):
#         x1,y1,z1 = loc[i]
#         x2,y2,z2 = loc[j]
#         cost = min(abs(x1-x2),abs(y1-y2),abs(z1-z2))
#         edges.append((cost,i,j))

for j in range(3):
    loc.sort(key=lambda data:data[j])
    before = loc[0][3]
    for i in range(1,N):
        cur_loc = loc[i][3]
        edges.append([abs(loc[i][j] - loc[i-1][j]),before, cur_loc])
        before = cur_loc
edges.sort()
for edge in edges:
    cost, a, b = edge
    if find(parent,a) != find(parent,b):
        union(parent,a,b)
        result +=cost
print(result)