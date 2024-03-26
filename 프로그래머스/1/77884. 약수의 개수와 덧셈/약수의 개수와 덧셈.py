def solution(left, right):
    list_a = []
    list_a2 = []
    T = 0
    for i in range(left, right + 1):
        list_a.append(i)
    for i in list_a:
        for i2 in range(1,i+1):
            if i % i2 == 0:
                list_a2.append(i2)
        if len(list_a2) % 2 == 0:
            T += i
            list_a2 = []
        else:
            T -= i
            list_a2 = []
        
    print(list_a, list_a2)
    print(T)
    return T