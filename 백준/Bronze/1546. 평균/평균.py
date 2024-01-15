N = int(input())
a = input().split()
b = list(map(int, a))
c = max(b)
d = 0
for i in range(N):
  b[i] = b[i]/c*100
  d = d + b[i]
print(d/N)