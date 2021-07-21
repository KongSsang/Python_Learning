def solution(participant, completion):
    answer = ''
    temp = 0
    
    for i in range(len(participant)):
        temp += hash(participant[i])

    for j in range(len(completion)):
        temp -= hash(participant[j])
        
    print(temp)

solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])
