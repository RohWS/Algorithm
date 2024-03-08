# 답은 1 1 2 2 2 8
A,B,C,D,E,F = map(int, input().split())
if A != 1:
  A = 1 - A
else:
  A = A - 1
  
if B != 1:
  B = 1 - B
else:
  B = B - 1
  
if C != 2:
  C = 2 - C
else:
  C = C - 2
  
if D != 2:
  D = 2 - D
else:
  D = D -2
  
if E != 2:
  E = 2 - E
else:
  E = E - 2
  
if F != 8:
  F = 8 - F
else:
  F = F - 8
print(A,B,C,D,E,F,"\n")