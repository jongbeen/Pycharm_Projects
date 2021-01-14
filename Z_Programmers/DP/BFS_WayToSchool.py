from collections import deque
INF = int(1e9)

dx = [0,1]
dy = [1,0]

def BFS(graph,n,m):
    # visited = [[False] * m for _ in range(n)]
    # visited[0][0] = True
    queue = deque([(0,0,0)])
    result = []
    while queue:
        x,y,cnt = queue.popleft()
        if x == n-1 and y == m-1:
            result.append(cnt)
        for nx, ny in zip(dx,dy):
            nx, ny = x+nx, y+ny
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] != INF:
                    queue.append((nx,ny,cnt+1))
    return result

def solution(m, n, puddles):
    graph = [[0]*m for _ in range(n)]
    for pud in puddles:
        x,y = pud
        graph[x-1][y-1] = INF
    answer = BFS(graph,n,m)
    ans = answer.count(min(answer))
    return ans

p = [[2,2]]
print(solution(4,3,p))