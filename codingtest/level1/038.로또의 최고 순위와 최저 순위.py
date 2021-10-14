def solution(lottos, win_nums):
    answer = []
    temp = 0
    zerocount = 0
    highest_temp = 0
    lowest_temp = 0
    for i in range(6):
        for j in range(6):
            if lottos[i] == win_nums[j]:
                temp += 1

    for i in range(6):
        if lottos[i] == 0:
            zerocount += 1

    highest_temp = temp + zerocount
    lowest_temp = temp

    x = 7 - highest_temp
    y = 7 - lowest_temp

    if highest_temp in [0,1]:
        x = 6
    if lowest_temp in [0,1]:
        y = 6

    answer.append(x)
    answer.append(y)

    return answer
