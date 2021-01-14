import sys
sys.stdin = open('input_3752.txt')

for tc in range(int(input())):
    N = int(input())
    array = list(map(int,input().split()))
    array.sort()
    start, SUM = min(array), sum(array)
    check = [False]*(SUM+1)
    for i in array:
        check[i] = True
    for i in range(start,SUM+1):
        for j in array:
            if i-j>=start and check[i-j] == True:
                check[i] = True
                break
    count = 0
    print(check)
    for i in range(start,SUM+1):
        if check[i]:
            count+=1
    tcnum = '#'+str(tc+1)
    print(tcnum, count)

