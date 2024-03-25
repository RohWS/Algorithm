T = int(input())
sub_T = 1000 - T
coin = 0
while True:
  if sub_T >= 500:
    coin += 1
    sub_T -= 500
  elif sub_T >= 100:
    sub_T -= 100
    coin += 1
  elif sub_T >= 50:
    sub_T -= 50
    coin += 1
  elif sub_T >= 10:
    sub_T -= 10
    coin += 1
  elif sub_T >= 5:
    sub_T -= 5
    coin += 1
  else:
    coin += sub_T
    break
print(coin)