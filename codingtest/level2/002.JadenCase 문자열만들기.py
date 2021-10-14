def solution(s):
    answer = ''
    s = s.lower()
    split_s = s.split(" ")

    for i in split_s:
        if i == '':
            answer += ' '
        elif i[0].isdigit() == True:
            if answer == '':
                answer += i
            else:
                answer = answer + ' ' + i
        else:
            i = i.capitalize()
            if answer == '':
                answer += i
            else:
                answer = answer + ' ' + i
    return answer

solution("3people   unFollowed me")
