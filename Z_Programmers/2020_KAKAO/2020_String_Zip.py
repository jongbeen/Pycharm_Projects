def solution(s):
    length = len(s)
    result = [length]
    for step in range(1,length+1):
        temp, combo, sum_value = [], 1, 0
        pre_word = s[0:step]
        for idx in range(step,length,step):
            cur_word = s[idx:idx+step]
            if pre_word == cur_word:
                combo += 1
                pre_word = cur_word
            else:
                if combo != 1:
                    temp.append(str(combo) + pre_word)
                else:
                    temp.append(pre_word)
                combo = 1
                pre_word = cur_word
        if combo != 1:
            temp.append(str(combo) + pre_word)
        else:
            temp.append(pre_word)
        # print(temp)
        for w in temp:
            sum_value += len(w)
        result.append(sum_value)

    answer = min(result)
    return answer

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcabcabcdededededede"))
