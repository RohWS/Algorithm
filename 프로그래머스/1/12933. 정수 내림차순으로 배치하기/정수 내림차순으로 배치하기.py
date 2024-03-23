def solution(n):
    list_n = list(str(n))
    list_n.sort(reverse=True)
    list_n = ''.join(list_n)
    return int(list_n)