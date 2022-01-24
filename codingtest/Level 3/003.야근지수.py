import heapq
def solution(n, works):
    answer = 0
    h_works = []
    for item in works:
        heapq.heappush(h_works, (-item, item))
    if sum(works) <= n:
        return 0
    else:
        for i in range(n):
            h_max = heapq.heappop(h_works)[1]
            h_max -= 1
            heapq.heappush(h_works, (-h_max, h_max))
        for i in range(len(h_works)):
            answer += h_works[i][1]**2

        return answer
    
solution(4, [4, 3, 3])