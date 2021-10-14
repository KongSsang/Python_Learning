from itertools import product
def solution(numbers, target):
    a = len(numbers)
    answer = 0
    for i in product(['+','-'], repeat = a):
        temp = 0
        cnt = 0
        for j in i:
            if j == '+':
                temp += numbers[cnt]
            else:
                temp -= numbers[cnt]
            cnt += 1
        if temp == target:
            answer += 1
    return answer

solution([1, 1, 1, 1, 1], 3)
