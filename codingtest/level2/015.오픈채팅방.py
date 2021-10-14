def solution(record):
    answer = []
    rec_2 = []
    id_name = {}
    for i in range(len(record)):
        rec_2.append(record[i].split())
    for i in range(len(rec_2)):
        if rec_2[i][0] == "Enter":
            id_name[rec_2[i][1]] = rec_2[i][2]
        elif rec_2[i][0] == "Change":
            id_name[rec_2[i][1]] = rec_2[i][2]
    for i in range(len(rec_2)):
        if rec_2[i][0] == "Enter":
            add = id_name[rec_2[i][1]] + "님이 들어왔습니다."
            answer.append(add)
        elif rec_2[i][0] == "Leave":
            add = id_name[rec_2[i][1]] + "님이 나갔습니다."
            answer.append(add)
    return answer

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])