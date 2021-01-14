from collections import deque

def BFS(graph,start,end):
    visited, count = [False] * (N+1), 0
    queue = deque([(start,count)])
    visited[start] = True
    while queue:
        node,count = queue.popleft()
        if node == end:
            print(count)
            break
        if graph[node] != []:
            for next_node in graph[node]:
                if 1<=next_node<=N and not visited[next_node]:
                    queue.append((next_node,count+1))
                    visited[next_node] = True
        for next_node in (node + 1,node-1):
            if 1<=next_node<=N and not visited[next_node]:
                queue.append((next_node, count + 1))
                visited[next_node] = True

N,M = map(int,input().split())
S,E = map(int,input().split())

array = [[] for _ in range(N+1)]
for _ in range(M):
    t_s,t_e = map(int,input().split())
    array[t_s].append(t_e)
    array[t_e].append(t_s)


BFS(array,S,E)