import sys
from heapq import heappush, heappop
sys.stdin = open('input_1249.txt','r')

INF = int(1e9)
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dijkstra(graph):
    distance, queue = [[INF]*N for _ in range(N)], []
    distance[0][0] = 0
    heappush(queue,[0,0,0])
    while queue:
        w, x, y = heappop(queue)
        if x == N-1 and y == N-1:
            return w
        for nx, ny in zip(dx, dy):
            nx, ny = x+nx, y+ny
            if 0<=nx<N and 0<=ny<N:
                nw = w + graph[nx][ny]
                if distance[nx][ny] > nw:
                    distance[nx][ny] = nw
                    heappush(queue,[nw,nx,ny])

# def dijkstra(graph):
#     distance, queue = [[INF]*N for _ in range(N)], []
#     distance[0][0] = 0
#     heappush(queue,[graph[0][0],0,0])
#     while queue:
#         w,x,y = heappop(queue)
#         if x == N-1 and y == N-1:
#             return w
#         for idx,idy in zip(dx,dy):
#             nx, ny = x + idx, y + idy
#             if 0<=nx<N and 0<= ny < N:
#                 nw = w + graph[nx][ny]
#                 if distance[nx][ny] > nw:
#                     distance[nx][ny] = nw
#                     heappush(queue,[nw,nx,ny])

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    graph = []
    for _ in range(N):
        graph.append(list(map(int,input())))
    result = dijkstra(graph)
    answer = "#{0} {1}".format(test_case, result)
    print(answer)
