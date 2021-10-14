def solution(s):
    a = len(s)
    answer = a
    temp = []
    cnt = 1
    fin_str = ''
    for i in range(1, a//2 + 1):
        temp2 = []
        temp = [s[j:j+i] for j in range(0, len(s), i)]
        temp.append('range')
        for k in range(1,len(temp)):
            if temp[k] == temp[k-1]:
                cnt += 1
            else:
                if cnt == 1:
                    temp2.append(temp[k-1])
                else:
                    temp2.append(str(cnt) + temp[k-1])
                    cnt = 1
        fin_str = ''.join(temp2)
        if answer < len(fin_str):
            pass
        else:
            answer = len(fin_str)
    return answer

solution("abcabcabcabcdededededede"	)