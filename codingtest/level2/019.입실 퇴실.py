def solution(enter, leave):
    answer = []
    process = []
    process2 = []
    for i in range(len(enter)):
        process.append(enter[i])
        process2.append(list(process))
        while True:
            if leave[0] in process:
                process.remove(leave[0])
                del leave[0]
                if len(leave) == 0:
                    break
                process2.append(list(process))
            else:
                break
    for i in process2:
        if len(i) == 1:
            process2.remove(i)
    for i in range(len(enter)):
        temp = []
        for j in process2:
            if i+1 in j:
                temp += j
        temp = set(temp)
        if len(temp) == 0:
            answer.append(0)
        else:
            answer.append(len(temp) - 1)
    print(answer)
    return answer
solution([1,4,2,3], [2,1,3,4])

