def solution(s):
    answer = True
    s = s.upper()
    p_count = s.count("P")
    y_count = s.count("Y")
    if p_count == y_count:
        return True
    else:
        return False
    print(p_count, y_count)
    return True