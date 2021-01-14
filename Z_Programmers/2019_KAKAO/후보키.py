from collections import deque
from itertools import combinations

def solution(relation):
    n_row = len(relation)
    n_col = len(relation[0])

    candidates = []
    for i in range(1, n_col+1):
        candidates.extend(combinations(range(n_col),i))
    final = []
    for keys in candidates:
        tmp = [tuple(item[key] for key in keys) for item in relation]
        # 1st tmp = [("100",),("200",)...("600",)]
        # 2nd tmp = [("100","ryan"),("200","apeach")...("600","apeach")]
        if len(set(tmp)) == n_row:
            final.append(keys)      #유일성 만족
    answer = set(final[:])
    print(answer)
    for i in range(len(final)):
        for j in range(i+1,len(final)):
            if len(final[i]) == len(set(final[i]).intersection(set(final[j]))):
                answer.discard(final[j])    # 존재하지 않는 자료 지워도 에러발생 X
    return len(answer)
relation = [["100","ryan","music","2"],
            ["200","apeach","math","2"],
            ["300","tube","computer","3"],
            ["400","con","computer","4"],
            ["500","muzi","music","3"],
            ["600","apeach","music","2"]]

print(solution(relation))