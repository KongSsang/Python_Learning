def solution(n):
    answer = 1
    for i in range(1,(n//2)+1):
        sum = 0
        for j in range(i,(n//2)+3):
            if sum == n:
                answer += 1
                break
            elif sum > n:
                break
            else:
                sum += j
    return answer
