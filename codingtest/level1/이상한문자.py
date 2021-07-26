def solution(s):
    alp_low = 'abcdefghijklmnopqrstuvwxyz'
    alp_upp = alp_low.upper()
    answer = ''
    l_s = []
    l_s = s.split(" ")

    for i in range(len(l_s)):
        y = 0
        for j in range(0,len(l_s[i])):
            if (y%2 == 1):
                temp = l_s[i][j]
                answer += temp.lower()
            else:
                temp = l_s[i][j]
                answer += temp.upper()
            y += 1
        if i == len(l_s)-1:
            break
        answer += ' '
    print(answer)
    return answer

solution('try hello world')