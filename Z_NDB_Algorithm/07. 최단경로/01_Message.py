from heapq import heappush, heappop
INF = int(1e9)

def dijkstra(graph, start):
    distance = [INF]*(N+1)
    distance[start] = 0
    queue = []
    heappush(queue,[0,start])
    while queue:
        cost,pos = heappop(queue)
        for p,c in graph[pos]:
            c += cost
            if distance[p] > c:
                distance[p] = c
                heappush(queue,[c,p])
    return distance

N, M, C = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, cost = map(int,input().split())
    graph[a].append((b,cost))

result,final = 0,0
ans = dijkstra(graph,C)

for i in ans:
    if i != INF and i != 0:
        final = max(final,i)
        result +=1
print(result,final)