from itertools import combinations

def solution(relation):
    tuples = len(relation)
    attributes = len(relation[0])
    n_att = [i for i in range(len(attributes))]
    candidates, final = [], []

    for i in range(1,attributes+1):
        candidates.extend(combinations(n_att,i))
    for keys in candidates:
        tmp = [tuple(item[key] for key in keys) for item in relation]
        if len(set(tmp)) == tuples:
            final.append(keys)
    answer = set(final)
    for i in range(len(final)):
        for j in range(i+1, len(final)):
            if len(final[j]) == len(set(final[i]).intersection(set(final[j]))):
                answer.discard(final[j])
    return len(answer)

relation = [["100","ryan","music","2"],
            ["200","apeach","math","2"],
            ["300","tube","computer","3"],
            ["400","con","computer","4"],
            ["500","muzi","music","3"],
            ["600","apeach","music","2"]]
print(solution(relation))