import sys
sys.stdin = open('input_2309.txt','r')
from itertools import combinations

hobit, answer = [], []
for _ in range(9):
    hobit.append(int(input()))
check = combinations(hobit,7)
for c in check:
    if sum(c) == 100:
        answer = list(c)
        answer.sort()
        break
for num in answer:
    print(num)
