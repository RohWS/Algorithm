N = int(input())

dic = {1: 0, 2: 1}

for i in range(3, N + 1):

  dic[i] = dic[i - 1] + 1

  if i % 3 == 0:
    dic[i] = min(dic[i // 3] + 1, dic[i])
  if i % 2 == 0:
    dic[i] = min(dic[i // 2] + 1, dic[i])

print(dic[N])