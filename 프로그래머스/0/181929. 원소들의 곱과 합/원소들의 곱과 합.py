def solution(num_list):
    N1 = 1
    N2 = 0
    for i in range(len(num_list)):
        N1 = N1 * num_list[i]
        N2 = sum(num_list)*sum(num_list)
    if N1 - N2 < 0:
        answer = 1
    else:
        answer = 0
    return answer