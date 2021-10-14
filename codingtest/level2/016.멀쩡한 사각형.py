from math import gcd
def solution(w,h):
    answer = 1
    a = min(w,h)
    b = max(w,h)
    if a ==1 :
        answer = 0
    else:
        answer = (w * h - ( w + h - gcd(w,h)))
    return answer