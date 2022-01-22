def solution(m, n, board):
    answer = 0
    board_list = []
    for i in range(max(m,n)):
        x = []
        for j in range(min(m,n)):
            x.append(board[j][i])
        board_list.append(x)
    while True:
        temp = []
        cnt = 0
        for i in range(max(m-1, n-1)):
            for j in range(min(m-1, n-1)):
                if board_list[i][j].isalpha() == True and board_list[i][j] == board_list[i][j+1] == board_list[i+1][j] == board_list[i+1][j+1]:
                    temp.append([i, j])
                    temp.append([i+1, j])
                    temp.append([i, j+1])
                    temp.append([i+1, j+1])
                    cnt += 1
        temp = set(list(map(tuple,temp)))
        temp = list(temp)
        
        for i in temp:
            x = i[0]
            y = i[1]
            board_list[x][y] = '0'
        for j in range(len(board_list)):
            z = board_list[j]
            cnt_0 = z.count('0')
            for k in range(cnt_0):
                z.remove('0')
            for k in range(cnt_0):
                z.insert(0, '0')
        if cnt == 0:
            break
    for i in board_list:
        answer += i.count('0')
    return answer

solution(4, 5, 	["CCBDE", "AAADE", "AAABF", "CCBBF"])



