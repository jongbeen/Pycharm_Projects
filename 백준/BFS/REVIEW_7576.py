from collections import deque
import sys
sys.stdin = open('input_7576.txt','r')

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def BFS(graph, start):
    queue = deque(start)
    while queue:
        x,y = queue.popleft()
        for idx, idy in zip(dx, dy):
            idx, idy = idx + x, idy + y
            if 0<=idx<N and 0<=idy<M:
                if graph[idx][idy] == 0:
                    graph[idx][idy] = graph[x][y] + 1
                    queue.append((idx,idy))
def check(graph):
    ans = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                return -1
            ans = max(ans, graph[i][j])
    return ans-1
M, N = map(int,input().split())
graph, start_queue = [], []
for _ in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            start_queue.append((i,j))
BFS(graph,start_queue)
answer = check(graph)
print(answer)