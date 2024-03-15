list_N = []
for i in range(5):
  N = int(input())
  if N <= 40:
    list_N.append(40)
  else:
    list_N.append(N)
T = sum(list_N) // 5
print(T)
  