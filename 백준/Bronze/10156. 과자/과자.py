K, N, M = map(int, input().split())
S = K * N - M
if S > 0:
  print(S)
elif S <= 0:
  print(0)