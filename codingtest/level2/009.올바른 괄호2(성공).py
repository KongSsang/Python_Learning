def solution(s):
    answer = True
    cnt = 0    
    if len(s)%2 == 0 and s[0] == '(' and s[-1] == ')' and s.count('(') == s.count(')'):
        for i in s:
            if cnt < 0:
                answer = False
            if i == '(':
                cnt += 1
            elif i == ')':
                cnt -= 1
    else:
        answer = False
    return answer

