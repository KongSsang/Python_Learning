def solution(n, t, m, p):
    answer = ''
    str_num = '0'
    for i in range(m*t+1):
        result = ''
        while i > 0:
            i, mod = divmod(i, n)
            if str(mod) == '10':
                result += 'A'
            elif str(mod) == '11':
                result += 'B'
            elif str(mod) == '12':
                result += 'C'
            elif str(mod) == '13':
                result += 'D'
            elif str(mod) == '14':
                result += 'E'
            elif str(mod) == '15':
                result += 'F'
            else:
                result += str(mod)
        result = result[::-1]
        str_num += result

    for i in range(p-1,len(str_num),m):
        answer += str_num[i]
        if len(answer) == t:
            break

    return answer
solution(2,16,2,1)