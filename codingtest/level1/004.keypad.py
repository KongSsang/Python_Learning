def solution(numbers, hand):
    
    def l_distance(a,b):
        l_dis = 0
        if a == b:
            l_dis = 0
        elif abs(a-b) in [1,3]:
            l_dis = 1
        elif abs(a-b) in [2,6]:
            l_dis = 2
        elif abs(a-b) in [5,9]:
            l_dis = 3
        else:
            l_dis = 4
        return l_dis

    def r_distance(c,d):
        r_dis = 0
        if c == d:
            r_dis = 0
        elif abs(c-d) in [1,3]:
            r_dis = 1
        elif abs(c-d) in [2,6]:
            r_dis = 2
        elif abs(c-d) in [5,9]:
            r_dis = 3
        else:
            r_dis = 4
        return r_dis


    answer = ''
    l_loc = 10
    r_loc = 12

    for i in numbers:
        if i in [1,4,7]:
            answer += 'L'
            l_loc = i
        elif i in [3,6,9]:
            answer += 'R'
            r_loc = i
        else:
            if i in [2,5,8]:
                if l_distance(i,l_loc) == r_distance(i,r_loc):
                    if hand == 'right':
                        answer += 'R'
                        r_loc = i
                    else:
                        answer += 'L'
                        l_loc = i 
                elif l_distance(i,l_loc) > r_distance(i,r_loc):
                    answer += 'R'
                    r_loc = i
                else:
                    answer += 'L'
                    l_loc = i
            else:
                i == 11
                if l_distance(i,l_loc) == r_distance(i,r_loc):
                    if hand == 'right':
                        answer += 'R'
                        r_loc = i
                    else:
                        answer += 'L'
                        l_loc = i 
                elif l_distance(i,l_loc) > r_distance(i,r_loc):
                    answer += 'R'
                    r_loc = i
                else:
                    answer += 'L'
                    l_loc = i
    return answer

