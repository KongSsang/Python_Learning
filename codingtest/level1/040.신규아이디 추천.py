def solution(new_id):
    answer = ''
    i = 0
    new_id_2 = []
    new_id_3 = []
    
    new_id = new_id.lower()

    for i in range(len(new_id)):
        if new_id[i] in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','-','_','.']:
            new_id_2.append(new_id[i])

    for i in range(len(new_id_2)):
        new_id_3.append(new_id_2[i])
        if len(new_id_3) >= 2:
            if new_id_3[-1] == '.':
                if new_id_3[-1] == new_id_3[-2]:
                    new_id_3.pop(-1)

    if new_id_3[0] == '.':
        new_id_3.pop(0)
    if len(new_id_3) > 0:
        if new_id_3[-1] == '.':
            new_id_3.pop(-1)

    if len(new_id_3) == 0:
        new_id_3.append('a')
        new_id_3 = new_id_3*3

    while True:
        if len(new_id_3) >= 16:
            new_id_3.pop(-1)
        else:
            break

    if new_id_3[-1] == '.':
        new_id_3.pop(-1)

    while True:
        if len(new_id_3) <= 2:
            new_id_3.append(new_id_3[-1])
        else:
            break
        
    answer = ''.join(new_id_3)
    print(answer)
    
    return answer