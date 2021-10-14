import math
def solution(nums):
    answer = 0
    result = []
    avdoverlap = []
    a = len(nums)
    primenum = []
    primenum2 = []
    

    for i in range(a):
        for j in range(a):
            for k in range(a):
                if i != j and i != k and j !=k and (str(i)+str(j)+str(k)) not in avdoverlap:
                    result.append(nums[i]+nums[j]+nums[k])
                    avdoverlap.append(str(i)+str(j)+str(k))
                    avdoverlap.append(str(i)+str(k)+str(j))
                    avdoverlap.append(str(j)+str(i)+str(k))
                    avdoverlap.append(str(j)+str(k)+str(i))
                    avdoverlap.append(str(k)+str(i)+str(j))
                    avdoverlap.append(str(k)+str(j)+str(i))
    
    for i in range(3000):
        for j in range(math.floor(i**0.5)):
            primenum.append(i % (j+1))
    
        if primenum.count(0) == 1:
            primenum2.append(i)
        primenum = []
     
    for i in result:
        if i in primenum2:
            answer += 1
    return answer

solution([1,2,3,4])
