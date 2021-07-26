def solution(num):
    answer = 0
    for i in range(500):
        if num == 1:
            break
        if (num%2) == 1:
            num = (num*3) + 1
        else:
            num = num/2
        answer += 1
        print(num)

    if answer == 500:
        answer = -1
    return answer

solution(6)