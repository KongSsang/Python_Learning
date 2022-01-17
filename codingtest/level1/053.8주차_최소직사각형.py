def solution(sizes):
    answer = 0
    ma = []
    mi = []
    for i in range(len(sizes)):
        ma.append(max(sizes[i]))
        mi.append(min(sizes[i]))
    answer = max(ma) * max(mi)
    print(answer)
    return answer

solution([[60, 50], [30, 70], [60, 30], [80, 40]])