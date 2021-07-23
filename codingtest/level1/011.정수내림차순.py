def solution(n):
    n_list = []
    n = str(n)
    for i in n:
        n_list.append(i)
    n_list = sorted(n_list, reverse=True)
    answer = str.join('', n_list)
    return int(answer)
