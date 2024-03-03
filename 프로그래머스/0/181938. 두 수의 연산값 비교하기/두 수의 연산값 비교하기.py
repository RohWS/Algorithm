def solution(a, b):
    N = int(str(a)+str(b))
    T = 2*a*b
    if N-T > 0:
        answer = N
    elif N-T < 0:
        answer = T
    else:
        answer = N
    return answer