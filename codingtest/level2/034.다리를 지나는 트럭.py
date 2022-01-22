def solution(bridge_length, weight, truck_weights):
    answer = 0
    ing = []
    wei = []
    if bridge_length == 1:
        answer = len(truck_weights)
    else:
        while True:
            if sum(wei) + truck_weights[0] <= weight:
                ing.append([truck_weights[0], answer])
                wei.append(truck_weights[0])
                truck_weights.pop(0)
                answer += 1
                if ing[0][1] + bridge_length == answer:
                    ing.pop(0)
                    wei.pop(0)
            else:
                answer += 1
                if ing[0][1] + bridge_length == answer:
                    ing.pop(0)
                    wei.pop(0)
            if len(truck_weights) == 0:
                answer += bridge_length
                break
    return answer

solution(100, 100, [10,10,10,10,10,10,10,10,10,10])