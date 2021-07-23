def solution(n):
    answer = 0
    list_2 = [0]
    for i in range(18):
        if n // (3**i) < 1:
            b = i
            break
    list_2 = list_2 * b

    for i in range(len(list_2)):
        temp = 3 ** (len(list_2)-1-i)
        if n // temp == 3:
            list_2[0] = 1
            break
        elif n // temp == 2:
            list_2[i] = 2
            n -= temp*2
        elif n // temp == 1:
            list_2[i] = 1
            n -= temp
        elif n // temp == 0:
            pass
    list_3 = list_2[::-1]

    for i in range(len(list_3)):
        temp2 = 3 ** (len(list_2)-1-i)
        if list_3[i] == 2:
            answer += temp2*2
        elif list_3[i] == 1:
            answer += temp2
        else:
            pass
    print(answer)
    return answer

solution(78413450)