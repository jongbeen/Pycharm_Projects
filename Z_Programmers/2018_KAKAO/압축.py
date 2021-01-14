from collections import defaultdict
def solution(msg):
    LZW = defaultdict()
    answer = []
    for i in range(26):
        word = chr(ord('A') + i)
        LZW[word] = i+1
    step, count = 1, 27
    for index in range(0,len(msg),step):
        w = msg[index:index+step]
        c = msg[index+step]
        new_str = w+c
        if new_str in LZW.keys():
            step += 1
            index -= 1
            continue
        else:
            LZW[new_str] = count
            count += 1

    return answer
lst = []
[lst.append(chr(i)) for i in range(ord('A'), ord('Z')+1)]
print(lst)