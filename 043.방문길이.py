def solution(dirs):
    answer = 0
    result = [[5, 5]]
    route = []
    route_2 = []
    a = 5
    b = 5
    for i in range(len(dirs)):
        if dirs[i] == 'U':
            if a == 0:
                pass
            else:
                a -= 1
        elif dirs[i] == 'D':
            if a == 10:
                pass
            else:
                a += 1
        elif dirs[i] == 'L':
            if b == 0:
                pass
            else:
                b -= 1
        else:
            if b == 10:
                pass
            else:
                b += 1
        result.append([a, b])
    for j in range(0, len(result) - 1):
        route.append([result[j], result[j+1]])


    for k in route:
        idx = [k[1],k[0]]
        if k not in route_2 and idx not in route_2 and k[0] != k[1]:
            route_2.append(k)
    return len(route_2)

print(solution("RRRRRRRRRRRRRRRRRRRRRUUUUUUUUUUUUULU"))