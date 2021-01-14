from heapq import heappush, heappop
import sys
sys.stdin = open('input_9370.txt', 'r')

INF = 1e9

def dijkstra(start,end):
    distance, queue, R = [INF] * (n + 1), [], []
    distance[start] = 0
    heappush(queue, [0, start])
    while queue:
        cost, pos = heappop(queue)
        for p, c in graph[pos]:
            c += cost
            if distance[p] > c:
                distance[p] = c
                heappush(queue, [c, p])
    return distance[end]

T = int(sys.stdin.readline())
answer = [[] for _ in range(T)]
for index in range(T):
    # n개 spot, m개 도로, t개 도착지 후보
    n,m,t = map(int,sys.stdin.readline().split())
    # s 출발, g와 h 도로는 무조건 지나야함
    s,g,h = map(int,sys.stdin.readline().split())
    graph,candidate,result = [[] for _ in range(n+1)], [],[]

    for _ in range(m):
        a,b,d = map(int,sys.stdin.readline().split())
        graph[a].append((b,d))
        graph[b].append((a,d))
    for _ in range(t):
        candidate.append(int(sys.stdin.readline()))

    for data in candidate:
        predict1 = dijkstra(s,g) + dijkstra(g,h)+dijkstra(h,data)
        predict2 = dijkstra(s,h) + dijkstra(h,g)+dijkstra(g,data)
        result = dijkstra(s,data)
        if predict1 == result or predict2 == result:
            answer[index].append(data)
    answer[index].sort()
for ans in answer:
    for data in ans:
        print(data, end = " ")
    print()

