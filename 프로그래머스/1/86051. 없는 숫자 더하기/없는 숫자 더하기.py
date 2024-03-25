def solution(numbers):
    N = 0
    for i in range(1,10):
        if i not in numbers:
            N += i
    return N