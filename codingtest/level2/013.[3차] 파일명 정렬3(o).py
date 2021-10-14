def solution(files):
    answer = []
    result = []
    for i in files:
        head = ''
        number = ''
        sort_number = '0'
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
                number = number[0:5]
                tail = number[5:]
            else:
                tail = ''
        else:
            if len(number) > 5:
                tail = i[temp2 - (len(number) - 5):]
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
        x = str(result[i][0]) + str(result[i][2]) + str(result[i][4])
        answer.append(x)
    return answer
solution(["img12.png", "img10.png", "img02.png", "img1.png", "i000" "IMG01.GIF", "img2000000"])