import sys
from collections import deque

sys.stdin = open('input_topology.txt','r')

v, e = map(int,input().split())
indegree = [0] * (v+1)
queue, graph = deque([]), [[] for _ in range(v+1)]
result = []

for _ in range(e):
    a, b = map(int,input().split())
    graph[a].append(b)
    indegree[b] +=1


for i in range(1, v+1):
    if indegree[i] == 0:
        queue.append(i)
while queue:
    node = queue.popleft()
    result.append(node)
    for i in graph[node]:
        indegree[i] -=1
        if indegree[i] == 0:
            queue.append(i)

for i in result:
    print(i, end=' ')