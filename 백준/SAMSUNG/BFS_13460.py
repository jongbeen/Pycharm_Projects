from collections import deque
import sys
sys.stdin = open('input_13460.txt','r')
sys.setrecursionlimit(1000)

dx = [0,0,1,-1]
dy = [1,-1,0,0]
directions = ["left","right","up","down"]

def go_left(graph, visited, x, y):
    move = 0
    while graph[x][y-1] == '.':
        if not visited[x][y-1]:
            y, move = y-1, move+1
            visited[x][y] = True
        else:
            break
    if graph[x][y-1] == 'O':
        visited[x][y-1] = True
        return x, y-1, move+1
    return x, y, move

def go_right(graph, visited, x, y):
    move = 0
    while graph[x][y+1] == '.':
        if not visited[x][y+1]:
            y, move = y+1, move+1
            visited[x][y] = True
        else:
            break
    if graph[x][y+1] == 'O':
        visited[x][y + 1] = True
        return x, y+1, move+1
    return x, y, move

def go_up(graph, visited, x, y):
    move = 0
    while graph[x-1][y] == '.':
        if not visited[x-1][y]:
            x, move = x+1, move+1
            visited[x][y] = True
        else:
            break
    if graph[x-1][y] == 'O':
        visited[x-1][y] = True
        return x-1, y, move+1
    return x, y, move

def go_down(graph, visited, x, y):
    move = 0
    while graph[x+1][y] == '.':
        if not visited[x+1][y]:
            x, move = x+1, move+1
            visited[x][y] = True
        else:
            break
    if graph[x+1][y] == 'O':
        visited[x + 1][y] = True
        return x+1, y, move+1
    return x, y, move

def BFS(graph,R,B,O):
    queue = deque([(R,0,B,0,0)])
    r_visited = b_visited = [[False]*M for _ in range(N)]
    x1,y1 = R
    x2,y2 = B
    r_visited[x1][y1], b_visited[x2][y2] = True, True
    while queue:
        R, r_move ,B ,b_move,cnt = queue.popleft()
        if B == O and R != O:
            return -1
        if R == O and B != O:
            if cnt <=10:
                return cnt
        r_x, r_y = R
        b_x, b_y = B
        print(r_x, r_y)
        for move in directions:
            if move == "left":
                r_x1, r_y1, r_move = go_left(graph, r_visited, r_x,r_y)
                b_x1, b_y1, b_move = go_left(graph, b_visited, b_x,b_y)
                r, b = (r_x1, r_y1), (b_x1, b_y1)
                queue.append((r,r_move,b,b_move,cnt+1))
            if move == "right":
                r_x1, r_y1, r_move = go_right(graph, r_visited, r_x, r_y)
                b_x1, b_y1, b_move = go_right(graph, b_visited, b_x, b_y)
                r, b = (r_x1, r_y1), (b_x1, b_y1)
                queue.append((r, r_move, b, b_move, cnt + 1))
            if move == "up":
                r_x1, r_y1, r_move = go_up(graph, r_visited, r_x, r_y)
                b_x1, b_y1, b_move = go_up(graph, b_visited, b_x, b_y)
                r, b = (r_x1, r_y1), (b_x1, b_y1)
                queue.append((r, r_move, b, b_move, cnt + 1))
            if move == "down":
                r_x1, r_y1, r_move = go_down(graph, r_visited, r_x, r_y)
                b_x1, b_y1, b_move = go_down(graph, b_visited, b_x, b_y)
                r, b = (r_x1, r_y1), (b_x1, b_y1)
                queue.append((r, r_move, b, b_move, cnt + 1))
    return -1

N, M = map(int,input().split())
graph = [[] for i in range(N)]
R,B,O = (0,0),(0,0),(0,0)
for i in range(N):
    temp = list(input())
    graph[i] = temp
    if 'R' in temp:
        j = temp.index('R')
        R = (i,j)
    if 'B' in temp:
        j = temp.index('B')
        B = (i,j)
    if 'O' in temp:
        j = temp.index('O')
        O = (i,j)
print(BFS(graph,R,B,O))

