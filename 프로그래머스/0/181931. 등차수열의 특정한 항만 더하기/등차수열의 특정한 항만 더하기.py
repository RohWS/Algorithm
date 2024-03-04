def solution(a, d, included):
    Nsum = 0
    for i, is_included in enumerate(included):
        if is_included:
            Nsum += a + (d * i)
    return Nsum