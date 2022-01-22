def solution(citations):
    answer = 0
    a = sorted(citations, reverse=True)
    for i in range(len(a)):
        if max(citations) == 0:
            answer = 0
            break
        elif min(citations) >= len(citations):
            answer += len(citations)
            break
        elif i >= a[i]:
            answer += i
            break
    return answer

solution([0, 1, 2])