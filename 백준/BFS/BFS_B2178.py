from collections import deque


N, M = map(int, input().split())
array = []
visited = [[False] * M for _ in range(N)]
for i in range(N):
    array.append(list(map(int, str(input()))))
count = 0
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
queue = deque([(0, 0, 1)])
result = 0

while queue:
    x, y, z = queue.popleft()
    if x == N - 1 and y == M - 1:
        result = z
        break

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny] and array[nx][ny] == 1:
                queue.append((nx, ny, z + 1))
print(result)