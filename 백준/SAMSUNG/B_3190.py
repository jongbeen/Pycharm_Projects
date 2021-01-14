from collections import deque

def move_body(body,dir):
    temp = []
    tx,ty = body.pop(0)
    dx, dy = dir
    itx, ity = tx+dx, ty+dy
    if 0<=itx< N and 0<=ity<N:
        temp.append((itx,ity))
    else:
        return -1
    while body:
        idx, idy = body.popleft()



def game(board, t_plan):
    init_body, init_dir = (0,0), (0,1)
    body, time = deque(init_body), 1
    while time:
        pass
# 모르겠음...

N = int(input())
board, t_plan = [[0]*(N) for _ in range(N)], []
K = int(input())
for _ in range(K):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1
L = int(input())
for _ in range(L):
    X, C = map(str, input().split())
    t_plan.append((int(X), C))

