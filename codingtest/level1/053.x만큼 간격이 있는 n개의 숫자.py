def solution(x, n):
    answer = []
    if x > 0:
        for i in range(x, n*x+1, x):
            answer.append(i)
    elif x < 0:
        for i in range(x,n*x-1,x):
            answer.append(i)
    else:
        for i in range(n):
            answer.append(0)
    return answer