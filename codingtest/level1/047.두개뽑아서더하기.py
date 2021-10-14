def solution(numbers):
    answer = []
    from itertools import combinations
    numbers = (list(combinations(numbers, 2)))
    for i in range(len(numbers)):
        answer.append(numbers[i][0]+numbers[i][1])
    answer = sorted(list(set(answer)))

    return answer

solution([2,1,3,4,1])