def solution(a, b):
    answer = ''
    annual = []
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    day = str(a)+str(b)
    for i in range(1,13):
        if i == 2:
            for j in range(1,30):
                annual.append(str(i)+str(j))
        elif i in [4,6,9,11]:        
            for j in range(1,31):
                annual.append(str(i)+str(j))
        else:
            for j in range(1,32):
                annual.append(str(i)+str(j))
                  
    answer = days[annual.index(day) % 7]

    return answer
