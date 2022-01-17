def solution(id_list, report, k):
    answer = [0] * len(id_list)
    cnt = {}
    sort_report = []
    ban_list = []
    for i in id_list:
        cnt[i] = 0
    report = set(report)
    for i in report:
        temp = i.split(" ")
        temp2 = cnt[temp[1]]
        temp2 += 1
        cnt[temp[1]] = temp2
    for key, value in cnt.items():
        if value >= k:
            ban_list.append(key)
    for i in report:
        temp = i.split(" ")
        if temp[1] in ban_list:
            answer[id_list.index(temp[0])] += 1
    return answer
    

solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)