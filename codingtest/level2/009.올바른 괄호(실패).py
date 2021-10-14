def solution(s):
    answer = False
    a = int(len(s)/2)
    
    if len(s)%2 == 0:
        s_forth = s[0:a]
        s_back = s[a:]
        c_1 = s_forth.count('(')
        c_2 = s_back.count(')')
        c_3 = s_forth.count(')')
        c_4 = s_back.count('(')
        if s_forth[0] == '('and s_back[-1] == ')' and (c_1 >= c_3) and (c_2 >= c_4) and c_1 == c_2 and c_3 == c_4:
            answer = True
        else:
            answer = False
    return answer

solution("())((())")
