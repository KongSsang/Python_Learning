from itertools import permutations
def solution(k, dungeons):
    answer = 0
    result = []
    a = list(permutations(dungeons, len(dungeons)))
    for i in range(len(a)):
        cnt = 0
        k_temp = k
        for j in range(len(dungeons)):
            if  k_temp >= a[i][j][0]:
                k_temp -= a[i][j][1]
                cnt += 1
            else:
                break
        result.append(cnt)
    answer = max(result)
    return answer

solution(80, [[80,20],[50,40],[30,10]])