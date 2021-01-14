import sys
from heapq import heappush, heappop
sys.stdin = open('input_1719.txt','r')

INF = int(1e9)

def dijkstra(graph,start,end):
    distance = [INF]*(N+1)
    distance[start] = 0
    queue, dist, r = [], INF, 0
    heappush(queue,[0,start])
    while queue:
        cost, pos = heappop(queue)
        for p,c in graph[pos]:
            c += cost
            if distance[p] > c:
                distance[p] = c
                heappush(queue,[c,p])
    for i in range(1, len(distance)):
        if distance[i] != 0:
            if dist > distance[i]:
                dist = distance[i]
                r = i
    return r

N, M = map(int,input().split())
graph, answer = [[] for _ in range(N+1)], [[INF]*(N+1) for _ in range (N+1)]
for _ in range(M):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

for i in range(1,N+1):
    for j in range(1,N+1):
        if i != j :
            answer[i][j] = dijkstra(graph,i,j)
for i in range(1,N+1):
    for j in range (1,N+1):
        if i==j:
            print("-", end=' ')
        else:
            print(answer[i][j], end =' ')
    print()
