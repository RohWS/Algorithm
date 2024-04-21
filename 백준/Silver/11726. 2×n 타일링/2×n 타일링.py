N = int(input())


d = [0] * (N + 5)
d[0] = 0
d[1] = 1
d[2] = 2
d[3] = 3

for i in range(4, N +1):
  d[i] = d[i-1] + d[i-2]
  
print(d[N] % 10007)
