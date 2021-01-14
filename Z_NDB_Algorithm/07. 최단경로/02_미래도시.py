import sys
INF = int(1e9)
sys.stdin = open('input_02.txt','r')

N,M = map(int,input().split())
graph = [[INF]*(N+1) for _ in range(N+1)]
for _ in range(M):
    S, E = map(int,input().split())
    graph[S][E] = 1
    graph[E][S] = 1
X, K = map(int,input().split())

for k in range(1,N+1):
    for a in range(1,N+1):
        for b in range(1,N+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
distance = graph[1][K] + graph[K][X]
if distance >= INF:
    print(-1)
else:
    print(distance)

