import sys
from heapq import heappush, heappop

sys.stdin = open('input_1249.txt','r')
INF = int(1e9)
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def dijkstra(graph,N):
    distance = [[INF]*N for _ in range(N)]
    distance[0][0] = 0
    queue, start = [], (0,0)
    heappush(queue,[0,start])
    while queue:
        cost, pos = heappop(queue)
        x,y = pos
        for nx,ny in zip(dx,dy):
            nx,ny = x+nx, y+ny
            if 0<=nx<N and 0<=ny<N:
                c = cost + graph[nx][ny]
                if distance[nx][ny] > c:
                    distance[nx][ny] = c
                    heappush(queue,[c,(nx,ny)])
    return distance[N-1][N-1]

for tc in range(int(input())):
    N = int(input())
    graph = []
    for _ in range(N):
        graph.append(list(map(int,input())))
    result = dijkstra(graph,N)
    tcnum = '#'+str(tc+1)
    print(tcnum,result)