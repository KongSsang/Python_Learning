def solution(arr):
    answer = []
    for i in range(len(arr)):
        answer.append(arr[i])
        if len(answer) > 1:
            if answer[-1] == answer[-2]:
                answer.pop(-1)
    return answer