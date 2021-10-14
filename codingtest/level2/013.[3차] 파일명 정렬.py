def solution(files):
    answer = []
    result = []
    for i in files:
        temp = 0
        temp2 = 0
        number = ''
        for j in range(len(i)):
            if (i[j].isdigit()):
                temp = j
                head = i[0:j]
                break
        for k in range(temp,len(i)):
            if (i[k].isdigit()):
                number += i[k]
            else:
                temp2 = k
                break
        if len(head) + len(number) == len(i):
            if len(number) > 5:
                tail = number[5:]
                number = number[:5]
            else:
                tail = ''
        else:
            if len(number) > 5:
                tail = number[5:] + i[temp2:]
                number = number[:5]
            else:
                tail = i[temp2:]

        for i in range(len(number)):
            if number[i] == '0':
                pass
            else:
                sort_number = number[i:]
                break
        sort_head = head.lower()
        result.append([head,sort_head,number,int(sort_number),tail])
    result.sort(key = lambda x: (x[1],x[3]))
    for i in range(len(result)):
        y = ''
        if result[i][4] == '':
            y = str(result[i][0]) + str(result[i][2])
            answer.append(y)
        else:
            y = str(result[i][0]) + str(result[i][2]) + str(result[i][4])
            answer.append(y)
    return answer

solution( ["a1.png", "b2.png", "a3.png", "img1.png", "IMG01.GIF", "sefefg214567gsg32t4","a0"])