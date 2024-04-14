def solution(array, height):
    m = 0
    for i in range(len(array)):
        if array[i] > height:
            m += 1
    return m