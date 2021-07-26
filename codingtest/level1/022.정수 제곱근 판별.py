def solution(n):
    answer = 0
    a = n**0.5
    if n/a == a and float(a) == int(a):
        answer = (a+1)**2
    else:
        answer = -1
    return answer
