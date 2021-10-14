import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    for i in range(len(scoville)-1):
        if scoville[0] >= K:
            break
        else:
            cnt += 1
            a = heapq.heappop(scoville)
            b = heapq.heappop(scoville)
            heapq.heappush(scoville, a + 2 * b)
        if len(scoville) == 1 and scoville[0] < K:
            cnt = -1
            break
    return cnt
solution([1, 2, 3, 9, 10, 12],7)