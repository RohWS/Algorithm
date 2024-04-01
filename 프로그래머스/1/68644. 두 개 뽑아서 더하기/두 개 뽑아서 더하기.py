from itertools import combinations, permutations
def solution(numbers):
    answer = []
    combi = list(combinations(numbers, 2))
    for i in range(len(combi)):
        answer.append(sum(combi[i]))
        set_answer = set(answer)
        answer = list(set_answer)
        answer_sort = answer.sort()
    return answer