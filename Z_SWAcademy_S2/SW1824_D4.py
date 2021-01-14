from collections import deque
import sys
sys.stdin = open('input_1824.txt','r')

def move(graph, location, direction):
    row, col = len(graph), len(graph[0])
    left, right, up, down = (0, -1), (0, 1), (-1, 0), (1, 0)
    x,y = location
    if direction == 0:
        dx, dy = left
        nx, ny = x+dx, y+dy
        if ny < 0:
            return nx, col-1
        else:
            return nx, ny
    elif direction == 1:
        dx, dy = right
        nx, ny = x + dx, y + dy
        if ny > col-1:
            return nx, 0
        else:
            return nx, ny
    elif direction == 2:
        dx, dy = up
        nx, ny = x + dx, y + dy
        if nx < 0:
            return row-1, ny
        else:
            return nx, ny
    else:
        dx, dy = down
        nx, ny = x + dx, y + dy
        if nx > row-1:
            return 0, ny
        else:
            return nx, ny

def BFS(graph):
    l,r,u,d = 0,1,2,3
    init_value, init_loc, init_d = graph[0][0], (0,0), r
    if '0'<=init_value<='9':
        init_value = int(init_value)
    else:
        init_value = 0
    queue = deque([(init_loc,init_d,init_value)])
    visited = [[[[False]* 16 for _ in range(4)] for _ in range(C)] for _ in range(R) ]
    visited[0][0][r][init_value] = True
    while queue:
        location, direction, value = queue.popleft()
        x, y = location
        sign = graph[x][y]
        if sign == '@':
            return "YES"

        if sign == '>':
            way = r
            idx, idy = move(graph, location, way)
            new_loc = (idx,idy)
            if not visited[idx][idy][r][value]:
                queue.append((new_loc,way,value))
                visited[idx][idy][r][value] = True

        if sign == '<':
            way = l
            idx, idy = move(graph, location, way)
            new_loc = (idx, idy)
            if not visited[idx][idy][l][value]:
                queue.append((new_loc, way, value))
                visited[idx][idy][l][value] = True

        if sign == '^':
            way = u
            idx, idy = move(graph, location, way)
            new_loc = (idx, idy)
            if not visited[idx][idy][u][value]:
                queue.append((new_loc, way, value))
                visited[idx][idy][u][value] = True

        if sign == 'v':
            way = d
            idx, idy = move(graph, location, way)
            new_loc = (idx, idy)
            if not visited[idx][idy][d][value]:
                queue.append((new_loc, way, value))
                visited[idx][idy][d][value] = True

        if sign == '-':
            if value == 0:
                value = 15
            else:
                value -= 1
            idx, idy = move(graph,location,direction)
            new_loc = (idx,idy)
            if not visited[idx][idy][direction][value]:
                queue.append((new_loc,direction,value))
                visited[idx][idy][direction][value] = True

        if sign == '+':
            if value == 15:
                value = 0
            else:
                value += 1
            idx, idy = move(graph, location, direction)
            new_loc = (idx, idy)
            if not visited[idx][idy][direction][value]:
                queue.append((new_loc, direction, value))
                visited[idx][idy][direction][value] = True

        if '0' <= sign <= '9':
            value = int(sign)
            idx, idy = move(graph, location, direction)
            new_loc = (idx, idy)
            if not visited[idx][idy][direction][value]:
                queue.append((new_loc, direction, value))
                visited[idx][idy][direction][value] = True

        if sign == '_':
            if value == 0:
                way = r
                idx, idy = move(graph, location, way)
                new_loc = (idx, idy)
                if not visited[idx][idy][r][value]:
                    queue.append((new_loc, way, value))
                    visited[idx][idy][way][value] = True
            else:
                way = l
                idx, idy = move(graph, location, way)
                new_loc = (idx, idy)
                if not visited[idx][idy][l][value]:
                    queue.append((new_loc, way, value))
                    visited[idx][idy][way][value] = True

        if sign == '|':
            if value == 0:
                way = d
                idx, idy = move(graph, location, way)
                new_loc = (idx, idy)
                if not visited[idx][idy][d][value]:
                    queue.append((new_loc, way, value))
                    visited[idx][idy][way][value] = True
            else:
                way = u
                idx, idy = move(graph, location, way)
                new_loc = (idx, idy)
                if not visited[idx][idy][u][value]:
                    queue.append((new_loc, way, value))
                    visited[idx][idy][way][value] = True

        if sign == '.':
            idx, idy = move(graph, location, direction)
            new_loc = (idx, idy)
            # print(idx,idy)
            if not visited[idx][idy][direction][value]:
                queue.append((new_loc, direction, value))
                visited[idx][idy][direction][value] = True

        if sign == '?':
            ways = [l,r,u,d]
            for way in ways:
                idx, idy = move(graph, location, way)
                new_loc = (idx,idy)
                if not visited[idx][idy][way][value]:
                    queue.append((new_loc, way, value))
                    visited[idx][idy][way][value] = True
    return "NO"


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    R,C = map(int,input().split())
    Array = []
    for _ in range(R):
        Array.append(list(input()))
    r = BFS(Array)
    print("#{0} {1}".format(test_case, r))
