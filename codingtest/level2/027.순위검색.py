def solution(info, query):
    answer = []
    for i in range(len(query)):
        result = 0
        for j in range(len(query[i]), 0, -1):
            if query[i][j].isdigit() == False:
                num = query[i][j:]
                query[i] = query[i][:j]
                abil = query[i].split("and")
                break
        for k in range(len(info)):
            cnt = 0
            for l in range(len(info[k]), 0, -1):
                if info[k][l].isdigit() == False:
                    num2 = info[k][l:]
                    break
            if int(num2) >= int(num):
                for m in range(len(abil)):
                    if "-" in abil[m]:
                        cnt += 1
                    else:
                        if abil[m] in info[k]:
                            cnt += 1
            else:
                pass
            if cnt == 4:
                result += 1
        answer.append(result)
    print(answer)
    return answer

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])