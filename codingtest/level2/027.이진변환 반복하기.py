def solution(s):
    a = 0
    b = 0
    while True:
        if s == "1":
            break
        a += 1
        temp2 = len(s)
        temp = s.count("1")
        s = "1"*temp
        b += temp2 - len(s)
        s = format(len(s),"b")
    return [a, b]

solution("110010101001")