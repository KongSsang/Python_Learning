def solution(s):
    answer = True
    cnt_p = s.count('p') + s.count('P')
    cnt_y = s.count('y') + s.count('Y')

    if cnt_p == cnt_y:
        answer = True
    else:
        answer = False
    return answer
