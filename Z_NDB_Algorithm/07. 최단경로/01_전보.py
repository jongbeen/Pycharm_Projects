from heapq import heappush, heappop
INF = int(1e9)

def djikstra(graph,start):
    distance, queue = [INF] * (N+1), []
    distance[start] = 0
    heappush(queue,[0,start])
    while queue:
        cost,pos = heappop(queue)
        for p,c in graph[pos]:
            c += cost
            if distance[p] > c:
                distance[p] = c
    count, S = 0,0
    for d in distance:
        if d != 0 and d!=INF:
            count += 1
            S = max(S,d)
    return count, S


N,M,C  = map(int,input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    x,y,z = map(int,input().split())
    graph[x].append((y,z))
print(djikstra(graph,C))