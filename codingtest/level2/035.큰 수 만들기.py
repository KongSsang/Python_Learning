def solution(number, k):
    results = []
    lenNumber = len(number)
    lenResult = lenNumber - k
    th = -1
    for i in range(lenResult):
        val = "0"
        for j in range(th+1, lenNumber -(lenResult - len(results))+1):
            
            if val < number[j]:
                th = j
                val = number[j]
                if val == "9": 
                    break
        results.append(val)
    answer = "".join(results)
    return answer


print(solution("4177252841", 4))