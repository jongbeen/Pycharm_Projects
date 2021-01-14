def check(str,i):
    if str[i] <'a' or str[i] >'z':
        return False
    if str[i+1] < 'a' or str[i+1] > 'z':
        return False
    return True

def Inter(s1_list,s2_list):
    inter = []
    s1_check = [False]*len(s1_list)
    s2_check = [False]*len(s2_list)
    for i in range(len(s1_list)):
        for j in range(len(s2_list)):
            if s1_list[i] == s2_list[j] and not s2_check[j]:
                s2_check[j] = True
                inter.append(s2_list[j])
                break
    return inter


def Union(s1_list,s2_list,inter):
    union = []
    union = s1_list + s2_list
    for i in inter:
        union.remove(i)
    return union


def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    s1_list,s2_list = [],[]
    for i in range(len(str1)-1):
        if check(str1,i):
            s1_list.append(str1[i]+str1[i+1])
    for i in range(len(str2)-1):
        if check(str2,i):
            s2_list.append(str2[i]+str2[i+1])
    # print(s1_list)
    # print(s2_list)
    inter = Inter(s1_list,s2_list)
    union = Union(s1_list,s2_list,inter)
    Ilen = len(inter)
    Ulen = len(union)
    if Ulen == 0 :
        return 65536
    return int((Ilen/Ulen)*65536)


# print(solution('FRANCE','french'))
# print(solution('handshake','shake hands'))
# print(solution('aa1+aa2','AAAA12'))
print(solution('E=M*C^2','e=m*c^2'))





