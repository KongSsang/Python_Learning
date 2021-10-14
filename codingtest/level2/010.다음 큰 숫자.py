def solution(n):
    b = format(n,'b')
    
    cnt = b.count('1')
    while True:
        n += 1
        temp = format(n,'b')
        temp = temp.count('1')
        if temp == cnt:
            break
    return n
solution(78)