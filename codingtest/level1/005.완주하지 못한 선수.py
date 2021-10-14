def solution(participant, completion):
    answer = ''
    temp = 0
    part = {}
    
    for i in participant:
        part[hash(i)] = i

    for i in range(len(participant)):
        temp += hash(participant[i])

    for j in range(len(completion)):
        temp -= hash(completion[j])

    answer = part[temp]
    
    return answer
