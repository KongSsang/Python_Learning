import operator
def solution(N, stages):
    value = []
    answer = []
    dic = {}
    for i in range(1,N+1):
        if (len(stages) > 0):
            if stages.count(i) == 0:
                value.append(0)
            else:
                temp = stages.count(i) / len(stages)
                value.append(temp)
                while True:
                    if stages.count(i) > 0:
                        stages.remove(i)
                    elif stages.count(i) == 0:
                        break
        else:
            value.append(0)

    for i in range(len(value)):
        dic[i+1] = value[i]


    dic = sorted(dic.items(), reverse=True, key=operator.itemgetter(1))
    
    for i in range(len(dic)):
        answer.append(dic[i][0])
    return answer

solution(5,	[4,4,4,4,4])