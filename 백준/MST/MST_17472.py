from collections import deque
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def BFS(i,j,graph,visited):
    t_nodes = []
    queue = deque([(i,j)])
    visited[i][j] = True
    while queue:
        x,y = queue.popleft()
        t_nodes.append((x,y))
        for nx,ny in zip(dx,dy):
            nx,ny = x+nx,y+ny
            if 0<=nx<N and 0<=ny<M:
                if graph[nx][ny] ==1:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
    return t_nodes

def BFS2(i,j,graph,node):
    queue = deque([(i,j)])
    pass

N, M = map(int, input().split())
graph, nodes, edges = [], [], []
visited = [[False]*M for _ in range(N)]

for _ in range(N):
    graph.append(list(map(int,input().split())))

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and not visited[i][j]:
            temp = BFS(i,j,graph,visited)
            nodes.append(temp)

for node in nodes:
    for x,y in node:
        pass



