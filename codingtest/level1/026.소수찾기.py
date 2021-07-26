def solution(n):
    ns = set(range(2,n+1))

    for i in range(2,n+1):
        if i in ns:
            ns -= set(range(i*2, n+1, i))

    return len(ns)