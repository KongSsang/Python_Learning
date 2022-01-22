def solution(n, left, right):
    answer = []
    result = []
    b = []
    start = left//n
    end =  right//n
    for i in range(start, (end + 1)):
        a = list(range(1, n+1))
        for j in range(i+1):
            a[j] = i+1
        b.append(a)
    for i in range(len(b)):
        for j in range(n):
            result.append(b[i][j])
    answer = result[left - start*n : right - (start * n) + 1]    
    return answer

solution(4, 7, 14)