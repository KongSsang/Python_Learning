def solution(n, lost, reserve):

    answer = 0
    student = [1]*n
    
    for i in lost:
        student[i-1] -= 1

    for i in reserve:
        student[i-1] += 1
    
    
    if student[0] == 2:
        if student[1] == 0:
            student[0] -= 1
            student[1] += 1
    elif student[n-1] == 2:
        if student[n-2] == 0:
            student[n-1] -= 1
            student[n-2] += 1

    for i in range(1,n-1):
        if student[i] == 2:
            if student[i-1] == 0:
                student[i] -= 1
                student[i-1] += 1
            elif student[i+1] == 0:
                student[i] -= 1
                student[i+1] +=1

    for i in range(n):
        if student[i] >= 1:
            answer += 1

    print(student)
    print(answer)

            
    return answer

solution(5,[2,4],[1,3,5])