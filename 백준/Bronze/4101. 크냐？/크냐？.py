while True:
  A, B = map(int, input().split())
  if A == 0 and B == 0:
    break
  if A - B > 0:
    print("Yes")
  elif A - B <= 0:
    print("No")