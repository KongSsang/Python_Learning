def solution(clothes):
    answer = 1
    dic = {}
    for i in range(len(clothes)):
        if i == 0:
            dic[clothes[i][1]] = 1
        else:
            if clothes[i][1] not in dic:
                dic[clothes[i][1]] = 1
            else:
                temp = dic[clothes[i][1]]
                temp += 1
                dic[clothes[i][1]] = temp
    
    a = dic.values()
    for i in a:
        answer *= i+1
    answer -= 1
    return answer

solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])