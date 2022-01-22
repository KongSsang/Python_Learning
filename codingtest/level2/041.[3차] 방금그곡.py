def solution(m, musicinfos):
    answer = '(None)'
    result = []
    y = []
    for i in range(len(m)):
            if m[i] == '#':
               y[-1] = y[-1].lower()
            else:
                y.append(m[i])
    m = ''.join(y)
    for i in musicinfos:
        x = []
        a = i.split(',')
        a[0] = a[0].split(':')
        a[1] = a[1].split(':')
        a[1] = ((int(a[1][0]) - int(a[0][0])) * 60) + (int(a[1][1]) - int(a[0][1]))
        del a[0]
        for i in range(len(a[2])):
            if a[2][i] == '#':
                x[-1] = x[-1].lower()
            else:
                x.append(a[2][i])
        a[2] = ''.join(x)
        temp = len(a[2])
        multi = (a[0] // temp) + 1
        a[2] *= multi
        a[2] = a[2][:a[0]]
        
        result.append(a)
    
    result = sorted(result, key = lambda x : -x[0])

    for i in range(len(result)):
        if m in result[i][2]:
            answer = result[i][1]
            return answer
    return answer
        

print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))