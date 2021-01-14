import sys
sys.setrecursionlimit(100000)
sys.stdin = open('input_1012.txt', 'r')

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def DFS(i,j,Graph):
    visited[i][j] = True
    for idx,idy in zip(dx,dy):
        nx, ny = i+idx, j+idy
        if 0<=nx<N and 0<=ny<M:
            if Graph[nx][ny] == 1 and not visited[nx][ny]:
                DFS(nx,ny,Graph)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0]*M for _ in range(N)]
    for _ in range(K):
        i,j = map(int,input().split())
        graph[j][i] = 1
    visited = [[False]*M for _ in range(N)]
    result = 0
    for x in range(len(graph)):
        for y in range(len(graph[x])):
            if not visited[x][y] and graph[x][y]:
                result+=1
                DFS(x,y,graph)
    print(result)







