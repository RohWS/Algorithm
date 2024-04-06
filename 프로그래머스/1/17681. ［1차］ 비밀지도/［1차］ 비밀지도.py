# def solution(n, arr1, arr2):
#     list_bin = list(bin(arr1[0]))
#     list_bin2 = list(bin(arr1[1]))
#     print(list_bin)
#     # print(list_bin[2:-1])
#     list_b = list_bin[2:]
#     print("list_b =", list_b)
#     list_b2 = list_bin2[2:]
#     print("list_b2 =", list_b2)
#     print(int(''.join(list_b)) | int(''.join(list_b2)))
#     print("그냥한거", arr1[0] | arr2[0])
#     print("비트연산 2인수", bin(arr1[0] | arr2[0]))
#     # print(bin(arr1[0]) | bin(arr1[1]))
#     answer = []
#     return answer

def solution(n, arr1, arr2):
    answer = []
    
    for marker1, marker2 in zip(arr1, arr2):
        binary = str(bin(marker1 | marker2))[2:]
        
        binary = '0' * (n - len(binary)) + binary
        
        binary = binary.replace('0', ' ')
        binary = binary.replace('1', '#')
        
        answer.append(binary)
    
    return answer
        