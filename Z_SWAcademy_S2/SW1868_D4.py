import sys
from collections import deque
sys.stdin = open('input_1868.txt','r')

T = int(input())
for test_case in range(1, T + 1):
    def find(graph, i, j):
        dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        dy = [-1, 0, 1, -1, 1, -1, 0, 1]
        count = 0
        for nx, ny in zip(dx, dy):
            idx, idy = i + nx, j + ny
            if 0 <= idx < N and 0 <= idy < N:
                if graph[idx][idy] == '*':
                    count += 1
        return count

    def BFS(graph,i,j):
        global total_count
        dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        dy = [-1, 0, 1, -1, 1, -1, 0, 1]
        que = deque([(i,j)])
        total_count += 1
        while que:
            i, j = que.popleft()
            visited[i][j] = True
            for nx, ny in zip(dx,dy):
                idx, idy = i + nx, j + ny
                if 0 <= idx < N and 0 <= idy < N:
                    if graph[idx][idy] != '*' and not visited[idx][idy]:
                        if graph[idx][idy] == 0 :
                            que.append((idx,idy))
                            visited[idx][idy] = True
                        else:
                            visited[idx][idy] = True

    N = int(input())
    graph, queue = [], deque([])
    visited = [[False]*N for _ in range(N)]
    total_count = 0

    for i in range(N):
        graph.append(list(map(str,input())))

    for i in range(N):
        for j in range(N):
            if graph[i][j] != '*':
                if graph[i][j] == '.':
                    graph[i][j] = find(graph,i,j)
                if graph[i][j] == 0:
                    queue.append((i,j))
            else:
                visited[i][j] = True
    while queue:
        x,y = queue.popleft()
        if not visited[x][y]:
            BFS(graph,x,y)

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                total_count += 1
    answer = "#{0} {1}".format(test_case,total_count)
    print(answer)