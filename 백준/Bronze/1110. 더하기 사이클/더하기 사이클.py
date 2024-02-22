N = int(input())
cycle = 1
tenN = N // 10
oneN = N % 10
sumN = tenN + oneN
NewN = oneN * 10 + sumN % 10
#print(cycle,tenN,oneN, sumN, NewN)
while N != NewN:
    cycle += 1
    tenN = NewN // 10
    oneN = NewN % 10
    sumN = tenN + oneN
    NewN = oneN * 10 + sumN % 10
    #print(NewN)
    
    #print(cycle,tenN,oneN,NewN)
print(cycle)