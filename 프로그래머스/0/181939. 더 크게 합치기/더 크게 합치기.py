def solution(a, b):
    A = str(a) + str(b)
    B = str(b) + str(a)
    answer = int(max(A,B))
    return answer