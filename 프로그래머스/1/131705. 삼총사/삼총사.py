import itertools

def solution(number):
    answer = 0
    c = list(itertools.combinations(number, 3))
    print(sum(c[0]))
    for i in range(len(c)):
        if sum(c[i]) == 0:
            answer += 1
    return answer