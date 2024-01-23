lllist=input()
a = len(lllist)
t=0
for i in range(a):
    if lllist[i] in "ABC":
        t=t+3
    elif lllist[i] in "DEF":
        t=t+4
    elif lllist[i] in "GHI":
        t=t+5
    elif lllist[i] in "JKL":
        t=t+6
    elif lllist[i] in "MNO":
        t=t+7
    elif lllist[i] in "PQRS":
        t=t+8
    elif lllist[i] in "TUV":
        t=t+9
    elif lllist[i] in "WXYZ":
        t=t+10
print(t)