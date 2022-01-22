def solution(s):
    answer = 0
    s = list(s)
    for i in range(len(s)):
        stack = []
        for j in range(len(s)):
            stack.append(s[j])
            temp = ''.join(stack[-2:]) 
            if temp == '()' or temp == '{}' or temp == '[]':
                stack.pop()
                stack.pop()
        if len(stack) == 0:
            answer += 1
        s.insert(len(s), s[0])
        del s[0]
    return answer

print(solution("([{)}]"))