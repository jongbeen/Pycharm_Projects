import sys
sys.stdin = open('input_2309.txt','r')
hobits = []
for _ in range(9):
    hobits.append(int(input()))
sum_hobit = sum(hobits)
one, two = 0, 0
for i in range(8):
    for j in range(i+1,9):
        if sum_hobit - (hobits[i] + hobits[j]) == 100:
            one = hobits[i]
            two = hobits[j]
            break
hobits.remove(one)
hobits.remove(two)
hobits.sort()
for num in hobits:
    print(num)