def solution(array):
    array.sort()
    a = len(array)
    a = a//2
    answer = array[a]
    return answer