T = int(input())
list_T = list()
for i in range(T):
  a = int(input())
  list_T.append(a)
list_T.sort()
for i2 in range(T):
  print(list_T[i2])
