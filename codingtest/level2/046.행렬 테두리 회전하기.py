def rotation(x, y):
    temp2 = 0
    adx = []
    a = x[0] - 1
    b = x[1] - 1
    c = x[2] - 1
    d = x[3] - 1
    for i in range(b, d):
        adx.append(y[a][i])
    for i in range(a, c):
        adx.append(y[i][d])
    for i in range(d, b, -1):
        adx.append(y[c][i])
    for i in range(c, a, -1):
        adx.append(y[i][b])
    adx.insert(0, adx[-1])
    del adx[-1]
    for i in range(b, d):
        y[a][i] = adx[temp2]
        temp2 += 1
    for i in range(a, c):
        y[i][d] = adx[temp2]
        temp2 += 1
    for i in range(d, b, -1):
        y[c][i] = adx[temp2]
        temp2 += 1
    for i in range(c, a, -1):
        y[i][b] = adx[temp2]
        temp2 += 1
    return y, min(adx)

def solution(rows, columns, queries):
    answer = []
    cnt = 0
    board = []
    for i in range(rows):
        temp = []
        for j in range(columns):
            cnt += 1
            temp.append(cnt)
        board.append(temp)
    for i in queries:
        a1, a2 = rotation(i, board)
        board = a1
        answer.append(a2)
    return answer

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))