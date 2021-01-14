from heapq import heappush, heappop
from collections import deque
import sys
sys.stdin = open("input_5719.txt", 'r')

INF = 1e9

def dijkstra(graph,start):
    distance[start],queue = 0,[]
    heappush(queue,[0,start])
    while queue:
        cost,pos = heappop(queue)
        for p,c in graph[pos]:
            c += cost
            if distance[p] > c and not dropped[pos][p]:
                distance[p] = c
                heappush(queue,[c,p])
def BFS(graph,end):
    queue = deque([end])
    while queue:
        node = queue.popleft()
        if node == start:
            break
        for prev, cost in graph[node]:
            if distance[node] == distance[prev]+cost:
                dropped[prev][node] = True
                queue.append(prev)

while True:
    N,M = map(int,input().split())
    if N ==0:
        break
    start,end = map(int,input().split())
    adj = [[] for _ in range(N+1)]
    reverse_adj = [[] for _ in range(N+1)]
    for _ in range(M):
        x,y,cost = map(int,input().split())
        adj[x].append((y,cost))
        reverse_adj[y].append((x,cost))
    distance = [INF]*(N+1)
    dropped = [[False]*(N+1) for _ in range(M+1)]
    dijkstra(adj,start)
    BFS(reverse_adj,end)
    distance = [INF] * (N + 1)
    dijkstra(adj,start)
    if distance[end] != INF:
        print(distance[end])
    else:
        print(-1)


