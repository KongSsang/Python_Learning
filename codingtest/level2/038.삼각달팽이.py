def solution(n):
    answer = []
    result = []
    pl = 1
    c_1 = 0
    c_2 = n-1
    c_3 = -1
    adx_1 = 0
    adx_2 = 1
    adx_3 = n-2
    x = 0
    for i in range(n):
        temp = [0]
        temp *= i+1
        result.append(temp)
    while n > 0:
        for i in range(n):
            result[i+adx_1][c_1] = pl
            pl += 1    
        n -= 1
        c_1 += 1
        adx_1 += 2
        if n == 0:
            break
        for i in range(n):
            result[c_2][i+adx_2] = pl
            pl += 1
        n -= 1
        c_2 -= 1
        adx_2 += 1
        if n == 0:
            break
        for i in range(n):
            result[adx_3-i][c_3] = pl
            pl +=1
        n -= 1
        c_3 -= 1
        adx_3 -= 1

    for i in range(len(result)):
        x += 1
        for j in range(x):
            answer.append(result[i][j])
    return answer

solution(6)
