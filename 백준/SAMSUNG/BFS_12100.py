from collections import deque
import sys
sys.stdin = open('input_12100.txt','r')

def go_left(board):
    n = len(board)
    temp, tmp = [], [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tmp[i][j] = board[i][j]
    for b in tmp:
        n, t, z = len(b), [], []
        while b:
            data = b.pop(0)
            if data != 0:
                t.append(data)
        k = 1
        for i in range(len(t)-1):
            if t[i] == t[i+1]:
                k += 1
        merged = False
        while t:
            d = t.pop(0)
            if not z:
                z.append(d)
            else:
                if z[-1] == d and not merged:
                    d2 = z.pop()
                    z.append(d2+d)
                    merged = True
                else:
                    merged = False
                    z.append(d)
        while z:
            d = z.pop(0)
            t.append(d)

        for _ in range(n-len(t)):
            t.insert(n-1,0)
        temp.append(t)
    return temp

def go_right(board):
    n = len(board)
    temp, tmp = [], [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tmp[i][j] = board[i][j]
    for b in tmp:
        n, t, z = len(b), [], []
        while b:
            data = b.pop()
            if data != 0:
                t.append(data)
        merged = False
        while t:
            d = t.pop(0)
            if not z:
                z.append(d)
            else:
                if z[-1] == d and not merged:
                    d2 = z.pop()
                    z.append(d2+d)
                    merged = True
                else:
                    merged = False
                    z.append(d)
        while z:
            d = z.pop()
            t.append(d)

        for _ in range(n-len(t)):
            t.insert(0,0)
        temp.append(t)
    return temp

def go_up(board):
    n = len(board)
    temp = [[0]*n for _ in range(n)]
    temp2 = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[j][i] = board[i][j]
    temp = go_left(temp)
    for j in range(n):
        for i in range(n):
            temp2[i][j] = temp[j][i]
    return temp2

def go_down(board):
    n = len(board)
    temp = [[0]*n for _ in range(n)]
    temp2 = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[j][i] = board[i][j]
    temp = go_right(temp)
    for j in range(n):
        for i in range(n):
            temp2[i][j] = temp[j][i]
    return temp2

def find_max(board):
    MAX = 0
    for b in board:
        MAX = max(MAX,max(b))
    return MAX

def solve(Board):
    queue = deque([(Board,0)])
    result = []
    directions = ["left","right","up","down"]
    while queue:
        board, cnt = queue.popleft()
        if cnt == 5:
            result.append(find_max(board))
        if cnt < 5:
            for move in directions:
                if move == "left":
                    temp_a = go_left(board)
                    queue.append((temp_a,cnt+1))
                if move == "right":
                    temp_b = go_right(board)
                    queue.append((temp_b,cnt+1))
                if move == "up":
                    temp_c = go_up(board)
                    queue.append((temp_c,cnt+1))
                if move == "down":
                    temp_d = go_left(board)
                    queue.append((temp_d,cnt+1))
    return max(result)
N = int(input())
Board = []
for _ in range(N):
    Board.append(list(map(int, input().split())))
print(solve(Board))
