import math
from itertools import combinations 
def solution(nums):
    answer = 0
    result = []
    a = len(nums)
    combi2 = []
    primenum = []
    primenum2 = []
    

    combi = list(combinations(nums, 3))
    for i in range(len(combi)):
        combi2.append(combi[i][0]+combi[i][1]+combi[i][2])

    for i in range(3000):
        for j in range(math.floor(i**0.5)):
            primenum.append(i % (j+1))
    
        if primenum.count(0) == 1:
            primenum2.append(i)
        primenum = []
     
    for i in combi2:
        if i in primenum2:
            answer += 1
    return answer

solution([1,2,3,4])
