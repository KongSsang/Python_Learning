import math
def solution(str1, str2):
    answer = 0
    str1 = str1.upper()
    str2 = str2.upper()
    set1 = []
    set2 = []
    intersection = []
    union = []
    for i in range(len(str1)-1):
        temp = str1[i:i+2]
        if temp.isalpha() == True:
            set1.append(temp)

    for j in range(len(str2)-1):
        temp = str2[j:j+2]
        if temp.isalpha() == True:
            set2.append(temp)
    
    if len(set1) == 0 and len(set2) == 0:
        return 65536
    elif len(set1) == 0 or len(set2) == 0:
        return 0
        
    for i in set2:
        union.append(i)

    while True:
        if set1[0] in set2:
            intersection.append(set1[0])
            set2.remove(set1[0])
            del set1[0]
        else:
            union.append(set1[0])
            del set1[0]
        if len(set1) == 0:
            break

    return math.trunc((len(intersection) / len(union)) * 65536) 

print(solution('E=M*c^2','def'))


