import sys
sys.stdin = open('input_2805.txt','r')

N, K = map(int,input().split())
array = list(map(int,input().split()))
array.sort()

start, end = 1, max(array)
while start <= end:
    mid, SUM = (start+end)//2, 0
    for i in array:
        if i>= mid:
            SUM += i-mid
    if SUM >= K:
        start = mid + 1
    else:
        end = mid - 1

print(end)


