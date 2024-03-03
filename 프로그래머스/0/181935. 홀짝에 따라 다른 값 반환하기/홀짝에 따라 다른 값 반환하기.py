def solution(n):
    n_list = []
    n_sum = 0
    i = 0
    n_even_sum = 0
    n_even = 0
    if n%2 ==0:
        for i3 in range(n):
            if i3%2 == 0:
                n_list.append(i3)
        for i4 in range(len(n_list)):
            n_even_sum = n_even_sum + (n_list[i4]*n_list[i4])
        answer = n_even_sum + n*n
    else:
        for i in range(n):
            if i%(2) != 0:
                n_list.append(i)
        for i2 in range(len(n_list)):
            n_sum = n_sum + n_list[i2]
        answer = n_sum + n

    return answer