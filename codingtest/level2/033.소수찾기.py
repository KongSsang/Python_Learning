from itertools import permutations 
import sys, math
def isPrime(x):
    if x <= 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True
def solution(numbers):
    answer = 0
    result = []
    adx = []
    for i in numbers:
        result.append(i)
    for i in range(1, len(result)+1):
        a = list(permutations(result, i))
        a = set(a)
        a = list(a)
        for j in range(len(a)):
            temp = ''.join(a[j])
            if isPrime(int(temp)) == True:
                adx.append(temp)
    for i in range(len(adx)):
        adx[i] = adx[i].lstrip("0")
    adx = set(adx)
    answer = len(adx)
    return answer

solution("011")
