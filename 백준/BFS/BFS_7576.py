from collections import deque
import sys

sys.stdin = open('input_7576.txt', 'r')
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

def BFS(graph):
    # visited = [[False] * M for _ in range(N)]
    queue = deque(start_point)
    while queue:
        x, y = queue.popleft()
        # visited[x][y] = True
        for nx, ny in zip(dx, dy):
            idx, idy = x + nx, y + ny
            if 0 <= idx < N and 0 <= idy < M:
                if graph[idx][idy] != -1 and graph[idx][idy] == 0:
                    graph[idx][idy] = graph[x][y] + 1
                    queue.append((idx, idy))
    return graph
def check(graph):
    Max = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                return -1
            Max = max(graph[i][j],Max)
    return Max-1

M, N = map(int, input().split())
graph, start_point = [], []

for _ in range(N):
    graph.append(list(map(int,input().split())))

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            start_point.append((i,j))

graph = BFS(graph)
print(check(graph))
