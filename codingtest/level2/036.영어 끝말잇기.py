import math
def solution(n, words):
    answer = []
    x = 0
    memory = [words[0]]
    for i in range(1, len(words)):
        if words[i] in memory or words[i][0] != memory[-1][-1] or len(words[i]) == 1:
            x = i + 1
            break
        elif words[i] not in memory:
            memory.append(words[i])
    if x == 0:
        answer = [0, 0]
    elif x % n == 0:
        answer = [n, math.ceil(x / n)]
    else:
        answer = [x % n, math.ceil(x / n)]
    return answer
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))