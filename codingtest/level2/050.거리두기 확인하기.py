def solution(places):
    answer = []
    for k in range(len(places)):
        result = 1
        for i in range(len(places)):
            for j in range(len(places)):
                temp = []
                if places[k][i][j] == "P":
                    if i-1 < 0:
                        temp.append(0)
                    else:
                        temp.append(places[k][i-1][j])
                    try:
                        temp.append(places[k][i][j+1])
                    except:
                        temp.append(0)
                    try:
                        temp.append(places[k][i+1][j])
                    except:
                        temp.append(0)
                    if j-1 < 0:
                        temp.append(0)
                    else:
                        temp.append(places[k][i][j-1])
                    if temp.count("P") > 0:
                        result = 0
                        break

                elif places[k][i][j] == "O":
                    if i-1 < 0:
                        temp.append(0)
                    else:
                        temp.append(places[k][i-1][j])
                    try:
                        temp.append(places[k][i][j+1])
                    except:
                        temp.append(0)
                    try:
                        temp.append(places[k][i+1][j])
                    except:
                        temp.append(0)
                    if j-1 < 0:
                        temp.append(0)
                    else:
                        temp.append(places[k][i][j-1])
                    if temp.count("P") > 1:
                        result = 0
                        break      
        answer.append(result)       
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))