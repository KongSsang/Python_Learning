import operator
def solution(strings, n):
    answer = []
    answer = sorted(strings)
    answer = sorted(answer, key=operator.itemgetter(n))
    return answer

solution(["abce", "abcd", "cdx"],2)