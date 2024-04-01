T = list(input())
# print(T)
ord_T = []
chr_T = []
for i in range(len(T)):
  ord_T.append(ord(T[i]))
# print(ord_T)
for i in range(len(ord_T)):
  if 90 >= ord_T[i] >= 65:
    ord_T[i] += 13
    if ord_T[i] > 90:
      ord_T[i] -= 26
  elif 122 >= ord_T[i] >= 97:
    ord_T[i] += 13
    if ord_T[i] > 122:
      ord_T[i] -= 26
for i in range(len(ord_T)):
  chr_T.append(chr(ord_T[i]))
# ''.join(chr_T)
print(''.join(chr_T))
