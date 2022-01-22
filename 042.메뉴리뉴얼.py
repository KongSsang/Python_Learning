from itertools import combinations
def solution(orders, course):
    answer = []
    for i in range(len(course)):
        result = []
        for j in range(len(orders)):
            temp = list(orders[j])
            a = (list(combinations(temp, course[i])))
            result += a
        for k in range(len(result)):
            result[k] = ''.join(result[k])
            so = sorted(result[k])
            result[k] = ''.join(so)
        count={}
        for i in result:
            try: count[i] += 1
            except: count[i]=1
        count = {key: value for key, value in count.items() if value != 1} 
        x = [k for k,v in count.items() if max(count.values()) == v]
        for i in x:
            answer.append(i)

    answer = sorted(answer)
    return answer

print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))