import sys
sys.stdin = open('input_1764.txt','r')

N, M = map(int,input().split())
arr1 , arr2 = set(), set()
for _ in range(N):
    arr1.add(input())
for _ in range(M):
    arr2.add(input())
result = list(arr1 & arr2)
result.sort()
print(len(result))
for i in result:
    print(i)
