def solution(answers):
    a = len(answers)

    student1 = []
    student2 = []
    student3 = []
    answer = []
    i = 0
    j = 0
    k = 0
    score1 = 0
    score2 = 0
    score3 = 0
    while True:
        student1.append(1)
        i += 1
        if i == a:
            break
        student1.append(2)
        i += 1
        if i == a:
            break
        student1.append(3)
        i += 1
        if i == a:
            break
        student1.append(4)
        i += 1
        if i == a:
            break
        student1.append(5)
        i += 1
        if i == a:
            break

    while True:
        student2.append(2)
        j += 1
        if j == a:
            break
        student2.append(1)
        j += 1
        if j == a:
            break
        student2.append(2)
        j += 1
        if j == a:
            break
        student2.append(3)
        j += 1
        if j == a:
            break
        student2.append(2)
        j += 1
        if j == a:
            break
        student2.append(4)
        j += 1
        if j == a:
            break
        student2.append(2)
        j += 1
        if j == a:
            break
        student2.append(5)
        j += 1
        if j == a:
            break
    
    while True:
        student3.append(3)
        k += 1
        if k == a:
            break
        student3.append(3)
        k += 1
        if k == a:
            break
        student3.append(1)
        k += 1
        if k == a:
            break
        student3.append(1)
        k += 1
        if k == a:
            break
        student3.append(2)
        k += 1
        if k == a:
            break
        student3.append(2)
        k += 1
        if k == a:
            break
        student3.append(4)
        k += 1
        if k == a:
            break
        student3.append(4)
        k += 1
        if k == a:
            break
        student3.append(5)
        k += 1
        if k == a:
            break
        student3.append(5)
        k += 1
        if k == a:
            break

    i = 0     

    for i in range(a):
        if student1[i] == answers[i]:
            score1 += 1
    print(score1)
    
    if score1 > score2 and score1 > score3:
        answer.append(1)
    elif score2 > score1 and score2 > score3:
        answer.append(2)
    elif score3 > score1 and score3 > score2:
        answer.append(3)
    elif score1 == score2 and score1 > score3:
        answer.append(1)
        answer.append(2)
    elif score1 == score3 and score1 > score2:
        answer.append(1)
        answer.append(3)
    elif score2 == score3 and score2 > score1:
        answer.append(2)
        answer.append(3)
    elif score1 == score2 == score3:
        answer.append(1)
        answer.append(2)
        answer.append(3)


    return answer

solution([1,2,3,4,5])
