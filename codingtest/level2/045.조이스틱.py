import string
def solution(name):
    answer = 0
    location = 0
    x = 1
    joy = list(name)
    a = list(string.ascii_uppercase)
    
    for i in range(len(name)):
        temp =  min(a.index(name[i]), 26-a.index(name[i]))
        answer += temp
    while True:
        loc_right = location + x
        loc_left = location - x
        if joy[loc_right] != 'A':
            joy[location] = 'A'
            location += x
            answer += 1
            x = 1
        elif joy[loc_left] != 'A':
            joy[location] = 'A'
            location -= x
            answer += 1
            x = 1
        elif joy[loc_right] == 'A' and joy[loc_left] == 'A':
            x += 1
            answer += 1
        if joy.count('A') == len(joy)-1:
            break
    return answer

print(solution("JAN"))