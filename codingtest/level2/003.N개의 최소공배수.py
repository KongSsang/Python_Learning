def solution(arr):
    answer = 0
    temp = 1
    N = 0
    for i in range(len(arr)):
        temp *= arr[i]
    for i in range(max(arr),temp+1):
        N = 0
        for j in arr:
            if i % j == 0:
                N += 1
        if N == len(arr):
            answer += i
            break
    return answer    
    
solution([2,6,8,14]	)