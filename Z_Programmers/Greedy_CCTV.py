def solution(routes):
    result,check = [],[]
    for r in routes:
        s,e = r
        distance = e-s
        result.append((s,e,distance))
    result.sort(key=lambda x:x[2])
    while result:
        cur = result.pop(0)
        start, dest, dist = cur

    answer = 0
    return answer