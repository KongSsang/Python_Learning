def solution(s):
    answer = 0
    temp = []
    for i in s:
        temp.append(i)
        if len(temp) > 1:
            if i == temp[-2]:
                temp.pop()
                temp.pop()
    if len(temp) == 0:
        answer = 1
    else:
        answer = 0
    return answer

solution('baaafaafaa')