N, M = map(int, input().split())
A, B = [], []
for i in range(N):
  r = list(map(int, input().split()))
  A.append(r)
for i2 in range(N):
  r = list(map(int, input().split()))
  B.append(r)
for i3 in range(N):
  for i4 in range(M):
    print(A[i3][i4]+B[i3][i4] ,end= ' ')
  print()