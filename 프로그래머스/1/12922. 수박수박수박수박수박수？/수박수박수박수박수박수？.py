def solution(n):
    w = n // 2
    if n % 2 == 0:
        answer = '수박' * w
    else:
        answer = '수박' * w + '수'
    return answer