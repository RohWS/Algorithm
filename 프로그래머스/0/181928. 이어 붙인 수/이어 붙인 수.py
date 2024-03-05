def solution(num_list):
    even_list = []
    odd_list = []
    for i in range(len(num_list)):
        if num_list[i]%2 == 0:
            even_list.append(str(num_list[i]))
        else:
            odd_list.append(str(num_list[i]))
    # print(even_list)
    # print(odd_list)
        
    str1 = "".join(even_list)
    str2 = "".join(odd_list)
    sum_list = int(str1) + int(str2)
    answer = sum_list
    return answer