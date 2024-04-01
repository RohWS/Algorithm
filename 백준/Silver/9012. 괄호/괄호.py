T = int(input())
for i in range(T):
  col = 0
  stack = list(map(str, input()))
  for i in range(len(stack)):
    if stack[i] == '(':
      col += 1
    elif stack[i] == ')':
      col -= 1
    if col < 0:
      col += 1000
  if col == 0:
    print("YES")
  else:
    print("NO")