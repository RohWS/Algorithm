N, M  = map(int, input().split())
a = []
for i in range(N):
  a.append(i+1)
for _ in range(M):
  num1, num2 = map(int, input().split())
  a[num1-1],a[num2-1] = a[num2-1],a[num1-1]
for i2 in range(N):
  print(a[i2],end=' ')