
def DFS(i,j,sign):
    visited[i][j] = True







def sqaure_move(Graph):
    N = len(Graph)
    key_tmp = [[0]*N for _ in range(N)]
    x,y=0,0
    for i in range(N-1,-1,-1):
        y = 0
        for j in range(N):
            key_tmp[x][y] = Graph[i][j]
            y+=1
        x+=1
    return key_tmp

def down_move(Graph):
    N = len(Graph)
    key_tmp = [[0]*N for _ in range(N)]
    for i in range(1,N-1):
        for j in range(N):
            key_tmp[i][j] = Graph[i-1][j]
    return key_tmp

def up_move(Graph):
    N = len(Graph)
    key_tmp = [[0] * N for _ in range(N)]
    for i in range(N-2, -1):
        for j in range(N):
            key_tmp[i][j] = Graph[i + 1][j]
    return key_tmp

def left_move(Graph):
    N = len(Graph)
    key_tmp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(1,N-1):
            key_tmp[i][j] = Graph[i][j + 1]
    return key_tmp

def right_move(Graph):
    N = len(Graph)
    key_tmp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N - 2, -1):
            key_tmp[i][j] = Graph[i][j -1]
    return key_tmp

def check(Graph):
    key_location = []
    N = len(Graph)
    for i in range(N):
        for j in range(N):
            if Graph[i][j] == 1:
                key_location.append((i,j))
    return key_location

def solution(key, lock):
    lockation, visited = [], [[False]*]
    for i in range(len(lock)):
        for j in range(len(lock[i])):
            if lock[i][j] == 0:
                lockation.append((i,j))


    answer = True
    return answer