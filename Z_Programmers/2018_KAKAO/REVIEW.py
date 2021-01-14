def find(m, n, graph):
    stack = []
    for i in range(m-1):
        for j in range(n-1):
            if graph[i][j] != ' ':
                if graph[i][j] == graph[i][j + 1] == graph[i + 1][j] == graph[i + 1][j + 1]:
                    stack.append((i,j))
    return stack
def check(m, n, graph):
    for i in range(m-1):
        for j in range(n-1):
            if graph[i][j] != ' ':
                if graph[i][j] == graph[i][j+1] == graph[i+1][j] == graph[i+1][j+1]:
                    return True
    return False
def remove_board(location,graph):
    while location:
        i, j = location.pop()
        graph[i][j] = '0'
        graph[i][j + 1] = '0'
        graph[i + 1][j] = '0'
        graph[i + 1][j + 1] = '0'

def drop_board(m, n, graph):
    words = []
    count = 0
    for i in range(n):
        word = ""
        for j in range(m):
            word += graph[j][i]
        c = word.count('0')
        count += c
        word = word.replace('0','')
        word = ' ' * c + word
        words.append(word)
    for i in range(n):
        for j in range(m):
            graph[j][i] = words[i][j]
    return count

def solution(m, n, board):
    # 높의 m, 폭 n mXn board
    graph = [[0]*n for _ in range(m)]
    answer = 0
    for i in range(m):
        for j in range(n):
            graph[i][j] = board[i][j]
    while check(m, n, graph):
        location = find(m,n,graph)
        remove_board(location,graph)
        answer += drop_board(m,n,graph)
    return answer

# B = ["TTTANT","RRFACC","RRRFCC",
#      "TRRRAA","TTMMMF","TMMTTJ"]
B = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
# print(solution(6,6,B))
print(solution(4,5,B))
# print("T00TT".replace('0',''))
