dx = [0,0,1,1]
dy = [0,1,0,1]

def safe(m,n,board,i,j):
    for x,y in zip(dx,dy):
        if i+x <0 or i+x>m-1 or j+y<0 or j+y>n-1:
            return False
    return True

def checkboard(i,j,board):
    boardSet = set()
    for x,y in zip(dx,dy):
        x,y = x+i,y+j
        boardSet.add(board[x][y])
    if len(boardSet) == 1 and boardSet != {" "}:
        return True
    return False

def del_block(board,i,j):
    for x,y in zip(dx,dy):
        x,y = x+i,y+j
        board[x][y] = ''
    return board

def drop_block(board,m,n):
    for i in range(n):
        col_str = ''
        for j in range(m):
            if board[j][i] != '':
                col_str += board[j][i]
        col_str = (m-len(col_str))*" "+col_str
        for j in range(m):
            board[j][i] = col_str[j]
    return board



def solution(m,n,board):
    board = [[block for block in row] for row in board]
    while True:
        del_list = []
        for i in range(m):
            for j in range(n):
                if safe(m,n,board,i,j):
                    if checkboard(i,j,board):
                        del_list.append((i,j))
        if len(del_list) == 0:
            break
        for del_pos in del_list:
            board = del_block(board,del_pos[0],del_pos[1])
        board = drop_block(board,m,n)
    return board

B = ["TTTANT","RRFACC","RRRFCC",
     "TRRRAA","TTMMMF","TMMTTJ"]
result = solution(6,6,B)
for data in result:
    print(data)


