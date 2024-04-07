def solution(array, commands):
    arr1 = []
    answer = []
    # print(len(commands))
    for i in range(len(commands)):
        arr1 = array[commands[i][0]-1:commands[i][1]]
        arr1.sort()
        print(arr1)
        answer.append(arr1[commands[i][2]-1])
    return answer