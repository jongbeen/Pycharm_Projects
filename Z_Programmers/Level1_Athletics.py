def solution(n, lost, reserve):
    cover = [-1,0,1]
    count = 0
    for l_item in lost:
        for c in cover:
            subs = l_item+c
            if subs in reserve:
                pt = reserve.index(subs)
                reserve.pop(pt)
                count+=1
                break
    print(reserve)
    return n-len(lost)+count

l,r = [2,4],[1,3,5]
print(solution(5,l,r))