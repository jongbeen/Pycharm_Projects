from collections import deque
import sys

sys.stdin = open('input_1012.txt', 'r')

dx = (0,0,-1,1)
dy = (1,-1,0,0)

def BFS(x,y):
    visited[x][y] = True
    queue = deque([(x,y)])
    while queue:
        x,y = queue.popleft()
        for idx,idy in zip(dx,dy):
            nx,ny = x+idx, y+idy
            if 0<=nx<N and 0<=ny<M:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    queue.append((nx,ny))
                    visited[nx][ny] = True

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0]*M for _ in range(N)]
    for _ in range(K):
        i,j = map(int,input().split())
        graph[j][i] = 1
    visited,count = [[False]*M for _ in range(N)],0
    for i in range(len(graph)):
        for j in range(len(graph)):
            if not visited[i][j] and graph[i][j] == 1:
                BFS(i,j)
                count += 1
    print(count)
    
