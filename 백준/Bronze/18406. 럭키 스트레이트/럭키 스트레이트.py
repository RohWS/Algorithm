T = list(map(int, (input())))
len_T = len(T)
L_T = 0
R_T = 0
for i in range(0, len_T//2):
  L_T += T[i]
for i2 in range(len_T//2, len_T):
  R_T += T[i2]
# print(L_T, R_T)
if L_T == R_T:
  print("LUCKY")
else:
  print("READY")