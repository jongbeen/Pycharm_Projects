from heapq import heappush, heappop

INF = 1e9
def DIJ(graph,start,end):
    distance = [INF] * (N+1)
    distance[start],queue = 0 , []
    heappush(queue,[0,start])
    while queue:
        cost,pos = heappop(queue)
        for p,c in graph[pos]:
            c += cost
            if distance[p] > c:
                distance[p] = c
                heappush(queue,[c,p])
    return distance[end]


N,M = map(int,input().split())
S,E = map(int,input().split())

graph = [[] for _ in range(N+1)]

for i in range(2,N):
    graph[i].append((i-1,1))
    graph[i].append((i+1,1))
graph[1].append((2,1))
graph[N].append((N-1,1))

for _ in range(M):
    t_s,t_e = map(int,input().split())
    graph[t_s].append((t_e,1))

print(DIJ(graph,S,E))