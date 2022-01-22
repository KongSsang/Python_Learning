import re
def solution(s):
    answer = []
    result = []
    s = s[1:-1]
    for i in range(len(s)):
        if s[i] == '{':
            a = i
        elif s[i] == '}':
            b = i
            x = s[a:b]
            temp = re.findall(r'\d+', x)
            result.append(temp)
    result.sort(key = len)
    for i in range(len(result)):
        for j in range(len(result[i])):
            if int(result[i][j]) not in answer:
                answer.append(int(result[i][j]))
    return answer

print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))