def solution(numbers):
    result = []
    for i in numbers:
        result.append(str(i))
    result.sort(key = lambda num: num*3, reverse = True)
    answer = ''.join(result)
    if len(answer) == answer.count('0'):
        answer = '0'
    return answer

solution([0, 0, 0, 0, 0])