def rev(u):
    u  = list(u)
    u.pop(0)
    u.pop()
    if u:
        temp = ''
        for item in u:
            if item == '(':
                temp += ')'
            else:
                temp += '('
        return temp

    return ''

def check_right(p):
    stack = []
    for word in p:
        if word == '(':
            stack.append(True)
        else:
            if stack:
                stack.pop()
            else:
                return False
    return True

def divide(p):
    for i in range(1, len(p)+1):
        u = p[:i]
        v = p[i:]
        left_count = u.count('(')
        right_count = u.count(')')
        if left_count == right_count:
            return u, v

def solution(p):
    answer = ''
    if p == '':
        return ''
    u,v = divide(p)
    if check_right(u):
        u = u + solution(v)
        return u
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        answer += rev(u)
    return answer

# print(solution(")("))
print(solution("()))((()"))