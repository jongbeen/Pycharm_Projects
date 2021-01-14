# 2진수, 8진수, 16진수 내장함수 존재
# bin(), oct(), hex()
# 10진수 -> int()사용
def tran(num,n):
    x = num
    y = ""
    if n <= 10:
        while x > 0:
            y = str(x % n) + y
            x //= n
    else:
        
    return y

def n_transition(n):
    stack = [0]
    for i in range(1,1000):
        num = tran(i,n)
        temp = list(map(int,num))
        stack.extend(temp)
    return stack

def solution(n, t, m, p):
    stack = n_transition(n)
    start, count = p-1, 0
    answer = ''
    while count < t:
        answer += str(stack[start])
        start += m
        count += 1
    return answer

print(solution(2,4,2,1))