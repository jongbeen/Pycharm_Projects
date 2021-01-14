from heapq import heappush, heappop
import sys
sys.stdin =  open('input_4485.txt', 'r')

INF = 1e9
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def DIJ(Graph,count):
    distance, queue = [[INF]*N for _ in range(N)], []
    heappush(queue,[Array[0][0],0,0])
    distance[0][0] = 0
    while queue:
        w,x,y = heappop(queue)
        if x == N-1 and y == N-1:
            print("Problem {0}: {1}".format(count,w))
            break
        for idx,idy in zip(dx,dy):
            nx,ny = x+idx,y+idy
            if 0<=nx<N and 0<=ny<N:
                nw = w+Graph[nx][ny]
                if distance[nx][ny] > nw:
                    distance[nx][ny] = nw
                    heappush(queue,[distance[nx][ny],nx,ny])

c=1
while True:
    N = int(input())
    if N == 0:
        break
    Array = [list(map(int,input().split())) for _ in range(N)]
    DIJ(Array,c)
    c+=1