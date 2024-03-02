def solution(str1, str2):
    str1_list = list(str1)
    str2_list = list(str2)
    new_list = []
    for i in range(len(str1_list)):
        new_list.append(str1_list[i])
        new_list.append(str2_list[i])
    answer = ''.join(new_list)
    return answer