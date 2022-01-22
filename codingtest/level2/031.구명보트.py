def solution(people, limit):
    answer = 0
    x = len(people)
    left = 0
    right = x - 1
    people = sorted(people)
    while True:
        if left == right:
            answer += 1
            break
        elif left > right:
            break
        else:
            if people[left] + people[right] > limit:
                right -= 1
                answer += 1
            else:
                left += 1
                right -= 1
                answer += 1
    return answer

solution([70, 50, 80, 50], 100)