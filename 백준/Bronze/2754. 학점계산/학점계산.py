T = list(input())
if T[0] == "A":
  S = 4.0
  if T[1] == "+":
    S = S + 0.3
  elif T[1] == "-":
    S = S - 0.3
elif T[0] == "B":
  S = 3.0
  if T[1] == "+":
    S = S + 0.3
  elif T[1] == "-":
    S = S - 0.3
elif T[0] == "C":
  S = 2.0
  if T[1] == "+":
    S = S + 0.3
  elif T[1] == "-":
    S = S - 0.3
elif T[0] == "D":
  S = 1.0
  if T[1] == "+":
    S = S + 0.3
  elif T[1] == "-":
    S = S - 0.3
else:
  S = 0.0
print(S)