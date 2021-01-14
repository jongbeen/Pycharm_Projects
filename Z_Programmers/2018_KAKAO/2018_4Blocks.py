def same(graph,i,j):
    v = graph[i][j]
    c1 = graph[i-1][j]
    c2 = graph[i][j-1]
    c3 = graph[i-1][j-1]
    if v == c1 and  v== c2 and  v == c3 and v != "0":
        return True
    return False
def check(graph):
    for i in range(1,len(graph)):
        for j in range(1,len(graph[0])):
            if same(graph,i,j):
                return True
    return False
def find(graph):
    temp = set()
    for i in range(1,len(graph)):
        for j in range(1,len(graph[0])):
            if same(graph,i,j):
                temp.add((i,j))
                temp.add((i-1, j))
                temp.add((i, j-1))
                temp.add((i-1, j-1))
    return temp

def solution(m,n,board):
    graph = []
    for i in range(m):
        graph.append(list(board[i]))
    while check(graph):
        place = find(graph)
        while place:
            x,y = place.pop()
            graph[x][y] = "0"

        temp = []
        for j in range(n):
            word, trs = "", ""
            for i in range(m):
                word += graph[i][j]
            word = word.replace("0","")
            trs = "0"*(m-len(word))+word
            temp.append(list(trs))
        for j in range(n):
            for i in range(m):
                graph[i][j] = temp[j][i]
    count = 0
    for i in range(m):
        for j in range(n):
            if graph[i][j] == "0":
                count+=1
    return count

b = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
print(solution(6,6,b))
