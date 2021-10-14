def solution(skill, skill_trees):
    answer = 0
    temp = []
    result = []
    for i in skill:
        temp.append(i)
    for i in range(len(skill_trees)):
        li = []
        for j in range(len(skill_trees[i])):
            if skill_trees[i][j] in temp:
                li.append(temp.index(skill_trees[i][j]))
        result.append(li)
    for i in range(len(result)):
        if len(result[i]) == 0:
            answer += 1
        elif len(result[i]) == len(skill):
            a = sorted(result[i])
            if result[i] == a:
                answer += 1
            else:
                pass
        elif len(result[i]) < len(skill):
            if 0 in result[i] and (max(result[i]) + 1) == len(result[i]):
                a = sorted(result[i])
                if result[i] == a:
                    answer += 1
                else:
                    pass
            else:
                pass
    print(answer)
    return answer

solution("CBD", ["BACDE", "CBADF", "AECB", "BDA","ZYRW"])