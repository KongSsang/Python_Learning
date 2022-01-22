def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book)
    for i in range(len(phone_book)-1):
        a = len(phone_book[i])
        if phone_book[i] == phone_book[i+1][:a]:
            answer = False
    return answer


solution(["119", "97674223", "1195524421"])