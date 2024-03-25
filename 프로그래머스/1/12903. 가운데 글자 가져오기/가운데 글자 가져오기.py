def solution(s):
    w = len(s)//2
    if len(s) % 2 == 0:
        answer = s[w-1]+s[w]
    else:
        answer = s[w]
    return answer