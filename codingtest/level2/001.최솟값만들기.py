def solution(A,B):
    answer = 0
    A_s = []
    B_s = []
    A_s = sorted(A)
    B_s = sorted(B, reverse=True)
    print(A_s)
    print(B_s)
    for i in range(len(A)):
        answer += (A[i] * B[i])
    

    return answer

solution([1, 4, 2],[5, 4, 4])
