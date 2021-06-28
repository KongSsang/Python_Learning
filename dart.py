def solution(dartResult):
    answer = 0
    answer1 = 0
    answer2 = 0
    answer3 = 0
    a = len(dartResult)
    dartResult = 'xx'+dartResult+'x'
    result = []
##########################################################    
    for i in range(2,a+2):
        if dartResult[i] in ['S','D','T']:
            if dartResult[i-1] == '0':
                if dartResult[i-2] == '1':
                    if dartResult[i+1] in ['*','#']:
                        result.append((dartResult[i-2]+dartResult[i-1]+dartResult[i]+dartResult[i+1]))
                    else:
                        result.append((dartResult[i-2]+dartResult[i-1]+dartResult[i]))
                else:
                    if dartResult[i+1] in ['*','#']:
                        result.append((dartResult[i-1]+dartResult[i]+dartResult[i+1]))
                    else:
                        result.append((dartResult[i-1]+dartResult[i]))
            else:
                if dartResult[i+1] in ['*','#']:
                    result.append((dartResult[i-1]+dartResult[i]+dartResult[i+1]))
                else:
                    result.append((dartResult[i-1]+dartResult[i]))
##########################################################
    formula1 = str(result[0])
    formula2 = str(result[1])
    formula3 = str(result[2])
    fm1 = 0
    fm2 = 0
    fm3 = 0
##########################################################
    if len(formula1) == 2:
        fm1 = int(formula1[0])
        if formula1[1] == 'S':
            answer1 += fm1
        elif formula1[1] == 'D':
            answer1 += fm1**2
        elif formula1[1] == 'T':
            answer1 += fm1**3
    elif len(formula1) == 3:
        if formula1[2] in ['*','#']:
            fm1 = int(formula1[0])
            if formula1[2] == '*':
                if formula1[1] == 'S':
                    answer1 += fm1*2
                elif formula1[1] == 'D':
                    answer1 += (fm1**2)*2
                elif formula1[1] == 'T':
                    answer1 += (fm1**3)*2
            elif formula1[2] == '#':
                if formula1[1] == 'S':
                    answer1 -= fm1
                elif formula1[1] == 'D':
                    answer1 -= fm1**2
                elif formula1[1] == 'T':
                    answer1 -= fm1**3
        elif formula1[2] in ['S','D','T']:
            if formula1[2] == 'S':
                answer1 += 10
            elif formula1[2] == 'D':
                answer1 += 100
            elif formula1[2] == 'T':
                answer1 += 1000
    elif len(formula1) == 4:
        if formula1[3] == '*':
            if formula1[2] == 'S':
                answer1 += 20
            elif formula1[2] == 'D':
                answer1 += 200
            elif formula1[2] == 'T':
                answer1 += 2000
        elif formula1[3] == '#':
            if formula1[2] == 'S':
                answer1 -= 10
            elif formula1[2] == 'D':
                answer1 -= 100
            elif formula1[2] == 'T':
                answer1 -= 1000
##########################################################
    if len(formula2) == 2:
        fm2 = int(formula2[0])
        if formula2[1] == 'S':
            answer2 += fm2
        elif formula2[1] == 'D':
            answer2 += (fm2**2)
        elif formula2[1] == 'T':
            answer2 += (fm2**3)
    elif len(formula2) == 3:
        if formula2[2] in ['*','#']:
            fm2 = int(formula2[0])
            if formula2[2] == '*':
                if formula2[1] == 'S':
                    answer2 += fm2*2
                    answer1 *= 2
                elif formula2[1] == 'D':
                    answer2 += (fm2**2)*2
                    answer1 *= 2
                elif formula2[1] == 'T':
                    answer2 += (fm2**3)*2
                    answer1 *= 2
            elif formula2[2] == '#':
                if formula2[1] == 'S':
                    answer2 -= fm2
                elif formula2[1] == 'D':
                    answer2 -= (fm2**2)
                elif formula2[1] == 'T':
                    answer2 -= (fm2**3)
        elif formula2[2] in ['S','D','T']:
            if formula2[2] == 'S':
                answer2 += 10
            elif formula2[2] == 'D':
                answer2 += 100
            elif formula2[2] == 'T':
                answer2 += 1000
    elif len(formula2) == 4:
        if formula2[3] == '*':
            if formula2[2] == 'S':
                answer2 += 20
                answer1 *= 2
            elif formula2[2] == 'D':
                answer2 += 200
                answer1 *= 2
            elif formula2[2] == 'T':
                answer2 += 2000
                answer1 *= 2
        elif formula2[3] == '#':
            if formula2[2] == 'S':
                answer2 -= 10
            elif formula2[2] == 'D':
                answer2 -= 100
            elif formula2[2] == 'T':
                answer2 -= 1000
##########################################################
    if len(formula3) == 2:
        fm3 = int(formula3[0])
        if formula3[1] == 'S':
            answer3 += fm3
        elif formula3[1] == 'D':
            answer3 += (fm3**2)
        elif formula3[1] == 'T':
            answer3 += (fm3**3)
    elif len(formula3) == 3:
        if formula3[2] in ['*','#']:
            fm3 = int(formula3[0])
            if formula3[2] == '*':
                if formula3[1] == 'S':
                    answer3 += fm3*2
                    answer2 *= 2
                elif formula3[1] == 'D':
                    answer3 += (fm3**2)*2
                    answer2 *= 2
                elif formula3[1] == 'T':
                    answer3 += (fm3**3)*2
                    answer2 *= 2
            elif formula3[2] == '#':
                if formula3[1] == 'S':
                    answer3 -= fm3
                elif formula3[1] == 'D':
                    answer3 -= (fm3**2)
                elif formula3[1] == 'T':
                    answer3 -= (fm3**3)
        elif formula3[2] in ['S','D','T']:
            if formula3[2] == 'S':
                answer3 += 10
            elif formula3[2] == 'D':
                answer3 += 100
            elif formula3[2] == 'T':
                answer3 += 1000
    elif len(formula3) == 4:
        if formula3[3] == '*':
            if formula3[2] == 'S':
                answer3 += 20
                answer2 *= 2
            elif formula3[2] == 'D':
                answer3 += 200
                answer2 *= 2
            elif formula3[2] == 'T':
                answer3 += 2000
                answer2 *= 2
        elif formula3[3] == '#':
            if formula3[2] == 'S':
                answer3 -= 10
            elif formula3[2] == 'D':
                answer3 -= 100
            elif formula3[2] == 'T':
                answer3 -= 1000      
            
    answer = (answer1+answer2+answer3)
    return answer

solution('0S#0S#0S#')