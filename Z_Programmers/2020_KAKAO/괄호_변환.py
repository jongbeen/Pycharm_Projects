def check_bal(p):
    opened = p.count('(')
    closed = p.count(')')
    if opened == closed:
        return True
    else:
        return False

def check_right(p):
    stack, ptr = [], 0
    for i in range(len(p)):
        if p[i] == '(':
            stack.append('(')
            ptr += 1
        else:
            if stack:
                stack.pop()
            else:
                return False
            ptr -= 1
            if ptr < 0 :
                return False
    return True

# def find_uv(p):
#     u_str, v_str = '', ''
#     for i in range(1, len(p)):
#         if check_bal(p[0:i]):
#             u_str = p[0:i]
#             v_str = p[i + 1:]
#             break
#     return u_str, v_str

def divide(p):
    openP, closeP = 0, 0

    for i in range(len(p)):
        if p[i] == '(':
            openP += 1
        else:
            closeP += 1
        if openP == closeP:
            return p[:i+1], p[i+1:]


def solution(p):
    if not p:
        return ""

    answer, u_str, v_str = '' , '', ''
    u_str, v_str = divide(p)

    if check_right(u_str):
        return u_str + solution(v_str)
    else:
        answer += '('
        answer += solution(v_str)
        answer += ')'

        for i in u_str[1:len(u_str) - 1]:
            if i == '(':
                answer += ')'
            else:
                answer += '('
        return answer

print(solution("(()())()"))
print(solution("()))((()"))

