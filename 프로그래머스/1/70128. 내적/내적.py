def solution(a, b):
    c = 0
    for i in range(len(a)):
        c = c + a[i] * b[i]
    return c