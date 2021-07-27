def solution(s):
    s = str(s)
    answer = False
    if len(s) == 4 and 6:
        for i in s:
            if i in ['0','1','2','3','4','5','6','7','8','9']:
                answer = True
                
            else:
                answer = False
                break
        
    return answer

solution('35a5')