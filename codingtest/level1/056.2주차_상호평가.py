def solution(scores):
    answer = ''
    score_sort = []
    score_avg = []
    for i in range(len(scores)):
        temp = []
        for j in range(len(scores)):
            temp.append(scores[j][i])
        if max(temp) == temp[i] or min(temp) == temp[i]:
            if temp.count(temp[i]) == 1:
                del temp[i]
        score_sort.append(temp)
    for i in range(len(score_sort)):
        score_avg.append(sum(score_sort[i]) / len(score_sort[i]))
    for i in score_avg:
        if i >= 90:
            answer += 'A'
        elif 90 > i >= 80:
            answer += 'B'
        elif 80 > i >= 70:
            answer += 'C'
        elif 70 > i >= 50:
            answer += 'D'
        else:
            answer += 'F'
    return answer

solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]])