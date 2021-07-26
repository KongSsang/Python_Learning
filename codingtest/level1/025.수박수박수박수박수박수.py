def solution(n):
    answer = ''
    i = 0
    while True:
        if i == n:
            break
        answer += '수'
        i += 1
        if i == n:
            break
        answer += '박'
        i += 1

    return answer