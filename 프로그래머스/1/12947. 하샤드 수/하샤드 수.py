def solution(x):
    y = []
    x = str(x)
    list_x = list(x)
    # print(list_x)
    for i in range(len(list_x)):
        y.append(int(x[i]))
    sum_y = sum(y)
    # print(y)
    # print(sum_y)
    if int(x) % sum_y != 0:
        answer = False
    else:
        answer = True
    return answer