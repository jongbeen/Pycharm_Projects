def solution(name):
    base, name = ["A"]*len(name), list(name)
    ptr, count = 0,0
    while base != name:
        toLeft, toRight = 1, 1
        if name[ptr] != base[ptr]:
            find = min((ord('Z') - ord(name[ptr]) + 1),(ord(name[ptr]) - ord('A')) )
            count += find
            name[ptr] = base[ptr]
        print(name)
        if base == name:
            break
        for i in range(1,len(name)):
            if name[ptr+i] == "A":
                toRight+=1
            else:
                break
        for i in range(1,len(name)):
            if name[ptr-i] == "A":
                toLeft+=1
            else:
                break
        print("ptr",ptr)
        print("left,right : ",toLeft, toRight)
        if toLeft >= toRight:
            ptr += toRight
            count += toRight
        else:
            ptr -= toLeft
            count += toLeft
    return count

print(solution("ABABAAAAABA"))
