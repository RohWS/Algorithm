N = int(input())


def fibo(N):
  f = []
  f.append(0)
  f.append(1)
  for i in range(2, N + 1):
    f.append(f[i - 1] + f[i - 2])
  return f[N]


print(fibo(N))
