from heapq import heappush, heappop
import sys
sys.stdin =  open('input_4485.txt', 'r')

INF = 1e9
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def dijkstra(Graph):
    distance = [[INF]*N for _ in range(N)]
    distance[0][0], queue = 0 , []
    heappush(queue,[Graph[0][0],0,0])
    #print(Graph)
    while queue:
        weight, x, y = heappop(queue)
        for idx,idy in zip(dx,dy):
            nx,ny = x+idx, y+idy
            if 0<=nx<N and 0<=ny<N:
                nweight = weight + Graph[nx][ny]
                if distance[nx][ny] > nweight:
                    distance[nx][ny] = nweight
                    heappush(queue,[distance[nx][ny],nx,ny])
    return distance[N-1][N-1]

result = []
while True:
    N = int(input())
    array = []
    if N == 0:
        break
    for _ in range(N):
        array.append(list(map(int,input().split())))
    answer = dijkstra(array)
    result.append(answer)
for i in range(len(result)):
    print("Problem {}: {value}".format(i+1,value = result[i]))



