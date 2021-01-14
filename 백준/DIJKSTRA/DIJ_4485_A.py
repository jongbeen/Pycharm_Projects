from heapq import heappush, heappop
import sys
sys.stdin =  open('input_4485.txt', 'r')

INF = 1e9

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dij(cnt):
    distance,queue = [[INF]*N for _ in range(N)],[]
    heappush(queue,[a[0][0],0,0])
    distance[0][0] = 0
    while queue:
        w,x,y = heappop(queue)
        if x == N-1 and y==N-1:
            print("Problem {0}:{1}".format(cnt,w))
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                nw = w + a[nx][ny]
                if distance[nx][ny] > nw:
                    distance[nx][ny] = nw
                    heappush(queue,[nw,nx,ny])
cnt=1
while True:
    N = int(input())
    if N==0:
        break
    a = [list(map(int,input().split())) for _ in range(N) ]
    dij(cnt)
    cnt+=1