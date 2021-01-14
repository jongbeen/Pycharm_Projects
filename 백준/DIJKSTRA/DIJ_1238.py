import sys
from heapq import heappush, heappop
sys.stdin = open('input_1238.txt','r')

INF = int(1e9)
def dijkstra(graph,start,dest):
    distance = [INF]* (N+1)
    distance[start], queue = 0, []
    heappush(queue,[0,start])
    while queue:
        cost, pos = heappop(queue)
        for p,c in graph[pos]:
            c += cost
            if distance[p] > c:
                distance[p] = c
                heappush(queue,[c,p])
    return distance[dest]

N, M, X = map(int, input().split())
graph, result = [ [] for _ in range(N+1) ], []
for _ in range(M):
    S, E, Time = map(int, input().split())
    graph[S].append((E,Time))
for i in range(1,N+1):
    if X != i:
        s, e = dijkstra(graph,i,X), dijkstra(graph,X,i)
        if s+e < INF:
            result.append(s+e)
print(max(result))

