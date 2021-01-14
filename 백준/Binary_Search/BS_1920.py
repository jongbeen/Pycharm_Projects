import sys
sys.stdin = open('input.1920.txt','r')

N = int(input())
array = list(map(int,input().split()))
array.sort()
M = int(input())
find = list(map(int,input().split()))
result = []
for i in find:
    start, end = 0, N-1
    result.append(0)
    while (start<=end):
        mid = (start+end)//2
        if i == array[mid]:
            result.pop()
            result.append(1)
            break
        if array[mid] > i:
            end = mid -1
        else :
            start = mid+1
for i in result:
    print(i)