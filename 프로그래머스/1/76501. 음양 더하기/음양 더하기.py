def solution(absolutes, signs):
    sum_a = []
    sub_a = []
    for i in range(len(absolutes)):
        if signs[i] == True:
            sum_a.append(absolutes[i])
        else:
            sub_a.append(absolutes[i])
    print(sum_a, sub_a)
    answer = sum(sum_a) - sum(sub_a)
    return answer