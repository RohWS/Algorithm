def solution(n):
    x = int(n**(1/2))
    if x * x == n:
        return (x + 1) * (x + 1)
    else:
        return -1