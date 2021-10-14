def solution(nums):
    answer = 0
    N = len(nums)/2
    nums = set(nums)
    nums = list(nums)
    if N < len(nums):
        answer += N
    else:
        answer += len(nums)
    return answer