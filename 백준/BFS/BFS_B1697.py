from collections import deque
Max = 10001
spot = [0] * Max

def BFS(start,end):
    visited = [False] * Max
    queue = deque([start])
    while queue:
        now = queue.popleft()
        if now == end:
            return spot[now]
        for next_pos in (now-1,now+1,now*2):
            if 0 <= next_pos < Max and not visited[next_pos]:
                spot[next_pos] = spot[now]+1


N,K = map(int,input().split())
print(BFS(N,K))



