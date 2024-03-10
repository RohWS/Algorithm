T = input()
T = list(T)
answer = 1
for i in range(len(T)//2+1):
  if T[i] != T[-1-i]:
    answer = 0
    
print(answer)