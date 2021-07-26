def solution(s, n):
    answer = ''
    from string import ascii_uppercase
    ua = list(ascii_uppercase)
    from string import ascii_lowercase
    la = list(ascii_lowercase)

    for i in range(len(s)):
        j = 0
        a = 0
        if s[i] in ua:
            j = ua.index(s[i])
            a = j + n
            if a > 25:
                a -= 26
            answer += ua[a]
        elif s[i] in la:
            j = la.index(s[i])
            a = j + n
            if a > 25:
                a -= 26
            answer += la[a]
        else:
            answer += ' '
    return answer
