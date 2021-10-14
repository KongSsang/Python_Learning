import numpy as np
from itertools import combinations
def solution(line):
    answer = []
    temp = list(combinations(line, 2))
    point = []
    x = []
    y = []
    for i in temp:
        C = [0,0]
        if ((i[0][0] * i[1][1]) - (i[0][1] * i[1][0])) == 0:
            pass
        else:
            C[0] = ((i[0][1] * i[1][2]) - (i[0][2] * i[1][1])) / ((i[0][0] * i[1][1]) - (i[0][1] * i[1][0]))
            C[1] = ((i[0][2] * i[1][0]) - (i[0][0] * i[1][2])) / ((i[0][0] * i[1][1]) - (i[0][1] * i[1][0]))
            if C[0].is_integer() == True and C[1].is_integer() == True:
                point.append([int(C[0]), int(C[1])])        

    for i in range(len(point)):
        x.append(point[i][0])
        y.append(point[i][1])

    x_max = max(x)
    x_min = min(x)
    y_max = max(y)
    y_min = min(y)

    print(x)
    print(y)

    if x_min < 0 and x_max > 0:
        for i in range(len(point)):
            x[i] = x_max - x[i]
    elif x_min > 0:
        for i in range(len(point)):
            x[i] -= x_min
    elif x_max < 0:
        for i in range(len(point)):
            x[i] += abs(x_min)
    elif x_min < 0 and x_max == 0:
        for i in range(len(point)):
            x[i] += abs(x_min)
    else:
        pass

    if y_min < 0 and y_max > 0:
        for i in range(len(point)):
            y[i] = y_max - y[i]
    elif y_min > 0:
        for i in range(len(point)):
            y[i] -= y_min
    elif y_max < 0:
        for i in range(len(point)):
            y[i] -= (y_min)
    elif y_min < 0 and y_max == 0:
        for i in range(len(point)):
            y[i] += abs(y_min)
    else:
        pass

    length = x_max - x_min + 1
    width = y_max - y_min + 1

    for i in range(width):
        answer.append('.' * length)

    for i in range(len(x)):
        point[i] = [y[i], x[i]]
    
    for i in point:
        li = []
        for j in range(len(answer[0])):
            li.append(answer[i[0]][j])
        li[i[1]] = '*'
        answer[i[0]] = ''.join(li)

    return answer

solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]])