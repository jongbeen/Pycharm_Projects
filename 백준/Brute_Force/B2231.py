N = int(input())
print_num = 0
for i in range(1,N+1):
    sum_i = sum(list(map(int,str(i)))) + i
    if sum_i == N:
        print_num = i
        break
print(print_num)