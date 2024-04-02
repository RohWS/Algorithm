T = input()
col = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
english = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
n = 0
for i in col:
  if T.count(i) >= 1:
    n += T.count(i)
    T = T.replace(i, " ")
for j in english:
  if T.count(j) >= 1:
    n += T.count(j)
    T = T.replace(j, " ")
print(n)