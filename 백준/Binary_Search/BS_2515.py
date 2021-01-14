import sys
sys.stdin = open('input_2515.txt','r')

N = int(input())
array = list(map(int,input().split()))
M = int(input())

start, end = 1, max(array)
while start <= end:
    mid, SUM = (start + end) // 2, 0
    for data in array:
        if data > mid:
            SUM += mid
        else:
            SUM += data
    if SUM <= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)