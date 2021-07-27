import operator
def solution(N, stages):
    stages = sorted(stages)
    stages2 = []
    value = []
    answer = []
    dic = {}
    for i in range(1,N+2):
        stages2.append(stages.count(i))
    s_s = sum(stages2)
    for i in range(len(stages2)):
        if s_s > 0:
            value.append(stages2[i]/s_s)
            s_s -= stages2[i]
        if s_s == 0:
            value.append(0)
    value.pop()
    value.pop()

    for i in range(len(value)):
        dic[i+1] = value[i]


    dic = sorted(dic.items(), reverse=True, key=operator.itemgetter(1))
    
    for i in range(len(dic)):
        answer.append(dic[i][0])
    return answer
