def solution(brown, yellow):
    answer = []
    result = []
    new_result = []
    if yellow == 1:
        result.append([1, 1])
    else:
        for i in range(1, yellow):
            if yellow % i == 0:
                result.append([max(i,yellow//i),min(i,yellow//i)])
    for v in result:
        if v not in new_result:
            new_result.append(v)
    for i in range(len(new_result)):
        if (((new_result[i][0] + 2) * 2) + new_result[i][1] * 2) == brown:
            answer = new_result[i]
    answer[0] += 2
    answer[1] += 2 
    return answer

solution(8, 1)