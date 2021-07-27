def solution(d, budget):
    d = sorted(d)
    answer = 0
    while True:
        temp = d[0]
        budget = budget - temp
        if budget < 0:
            break
        answer += 1
        del d[0]
        if len(d) == 0 or budget == 0:
            break
    return answer
solution([1,3,2,5,4],9)