from heapq import heappush, heappop
import sys
sys.stdin =  open('input_10282.txt', 'r')
INF = 1e9

def dijkstra(start):
    distance = [INF]*(N+1)
    queue, distance[start] = [], 0
    heappush(queue,[0,start])
    while queue:
        cost,pos = heappop(queue)
        for p,c in Graph[pos]:
            c += cost
            if distance[p] > c:
                distance[p] = c
                heappush(queue,[c,p])
    return distance

for _ in range(int(input())):
    N,D,C = map(int,input().split())
    Graph = [[] for _ in range(N+1)]
    for _ in range(D):
        a,b,s = map(int,input().split())
        Graph[b].append((a,s))
    result = dijkstra(C)
    Max, count, answer = -1, 0, []
    for i in range(len(result)):
        if result[i] != INF:
            count += 1
            answer.append(result[i])
    print(count, max(answer))