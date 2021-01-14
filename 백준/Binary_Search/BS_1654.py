import sys
sys.stdin = open('input_1654.txt','r')
sys.setrecursionlimit(10000)

N, K = map(int,input().split())
array = []
for _ in range(N):
    array.append(int(input()))
array.sort()
start, end = 1, max(array)

while start <= end:
    mid = (start + end) // 2
    lines = 0
    for i in array:
        lines += i // mid
    if lines >= K:
        start = mid + 1
    else:
        end = mid - 1
print(end)