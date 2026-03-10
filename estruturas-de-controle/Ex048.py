#Soma de ímpares múltiplos de 3

s=0
for c in range(1,501):
    if c%2 == 0:
        continue
    elif c%3!=0:
        continue
    s+=c
print(s)



