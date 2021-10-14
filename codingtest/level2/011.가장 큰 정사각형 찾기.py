def solution(board):
    answer = 0
    for i in range(len(board)-1,-1,-1):
        for j in range(len(board[0])-1,-1,-1):
            if board[i][j] == 1:
                temp = min(i,j)
                a = 1
                for k in range(j,j-temp-1,-1):
                    for l in range(i,i-temp-1,-1):
                        a *= board[k][l]

        if a == 1:
            answer = (temp+1)**2
            break
    return answer

solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]])

