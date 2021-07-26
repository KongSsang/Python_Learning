def solution(x):
    answer = True
    N = [int(i) for i in str(x)]
    temp = sum(N)

    if (int(x)%temp) == 0:
        answer = True
    else:
        answer = False
    return answer

solution(132)