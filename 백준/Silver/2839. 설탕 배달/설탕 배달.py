T = int(input())
bag = 0
while T >= 0:
  if T % 5 == 0:
    bag = bag + T // 5
    print(bag)
    break
  T -= 3
  bag += 1
else:
  bag = -1
  print(bag)