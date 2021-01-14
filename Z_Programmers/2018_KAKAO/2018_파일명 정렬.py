def check(file):
    head, number, tail = '', '', ''
    check_head = True
    for index in range(len(file)):
        if '0'<= file[index] <='9' or check_head:
            if '0'<= file[index] <= '9':
                number += file[index]
                check_head = False
            else:
                head += file[index]
        else:
            tail = file[index:]
            break
    return head, number, tail
def solution(files):
    stack, order = [],0
    answer = []
    for file in files:
        head, number, tail = check(file)
        h = head.lower()
        stack.append((h,int(number),order,head,number,tail))
        order += 1
    stack = sorted(stack, key = lambda x:(x[0],x[1],x[2]))
    for data in stack:
        w = data[3]+data[4]+data[5]
        answer.append(w)
    return answer

arr = ["img12.png", "img10.png", "img2.png", "img1.png"]
arr2 = "muzi1.txt", "MUZI1.txt", "muzi001.txt", "muzi1.TXT"
arr3 = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
d = solution(arr3)
for i in d:
    print(i)