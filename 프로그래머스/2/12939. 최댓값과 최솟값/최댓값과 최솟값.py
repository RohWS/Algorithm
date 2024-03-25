def solution(s):
    m = []
    s = list(map(int, s.split()))
    m.append(min(s))
    m.append(max(s))
    answer = f'{m[0]} {m[1]}'
    return answer