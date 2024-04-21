import sys

n, k = map(int, sys.stdin.readline().split())
C = []
for i in range(n):
  x = int(sys.stdin.readline())
  if (x <= k):
    C.append(x) 

if (len(C) == 0):  
  print(0)
else:
  s = [0 for i in range(k)]  
  for i in range(len(C)):  
    s[C[i] - 1] += 1  
    for j in range(C[i], k): 
      s[j] += s[j - C[i]] 
  print(s[k - 1])
