from bisect import bisect_left, bisect_right
# import sys
# sys.stdin = open('input_10816.txt','r')

N = int(input())
array = list(map(int,input().split()))
array.sort()

M = int(input())
pack = list(map(int,input().split()))
result = []
for i in pack:
    l = bisect_left(array,i)
    r = bisect_right(array,i)
    result.append(r-l)
for i in result:
    print(i, end=' ')
