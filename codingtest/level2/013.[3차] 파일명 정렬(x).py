def solution(files):
    answer = []
    result = []
    for i in files:
        head = ''
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
            tail = ''
            pass
        elif temp2 != len(i):
            tail = i[temp2::]
        else:
            tail = ''
        if len(number) > 5:
            number = number[0:5]
            tail = number[3:] + tail
        for i in range(len(number)):
            if number[i] == '0':
                pass
            else:
                sort_number = number[i::]
                break
        sort_head = head.lower()
        result.append([head,sort_head,number,int(sort_number),tail])
    print(result)
    result.sort(key = lambda x: (x[1],x[3]))
    for i in range(len(result)):
        x = str(result[i][0]) + str(result[i][2]) + str(result[i][4])
        answer.append(x)
    return answer

solution( ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2000000", "i0"])