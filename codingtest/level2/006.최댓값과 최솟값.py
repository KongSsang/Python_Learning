def solution(s):
    answer = ''
    s = s.split()
    temp = []
    for i in range(len(s)):
        temp.append(int(s[i]))
    a = min(temp)
    b = max(temp)
    answer = str(a) +' ' + str(b)
    return answer
solution("-1 -2 -3 -4")
