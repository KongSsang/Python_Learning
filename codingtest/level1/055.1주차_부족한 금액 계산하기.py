def solution(price, money, count):
    answer = -1
    total_price = 0
    for i in range(count):
        plus = price * (i+1)
        total_price += plus
    answer = total_price - money
    if answer <= 0:
        answer = 0
    return answer

solution(3, 20, 4)