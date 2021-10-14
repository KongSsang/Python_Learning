import numpy as np
def solution(arr1, arr2):
    answer = []
    ar1 = np.array(arr1)
    ar2 = np.array(arr2)
    multi = ar1.dot(ar2)
    answer = multi.tolist()
    return answer
solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]],[[5, 4, 3], [2, 4, 1], [3, 1, 1]])