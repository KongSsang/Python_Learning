def solution(n, arr1, arr2):
    answer = []
    arr1_2 = []
    arr2_2 = []
    
    for i in range(n):
        bi = format(arr1[i],'b')
        bi_2 = format(arr2[i],'b')
        if len(bi) < n:
            z = '0'
            cnt_z = n - len(bi)
            z = z * cnt_z
            bi = z + bi
        arr1_2.append(bi)
        if len(bi_2) < n:
            z = '0'
            cnt_z = n - len(bi_2)
            z = z * cnt_z
            bi_2 = z + bi_2
        arr2_2.append(bi_2)
    for i in range(n):
        temp = ''
        for j in range(n):
            if arr1_2[i][j] == arr2_2[i][j] == '0':
                temp += ' '
            else:
                temp += '#'
        answer.append(temp)
    return answer

