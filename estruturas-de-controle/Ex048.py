#Soma de ímpares múltiplos de 3

s=0
c=0
n=int(input('Qual o número?'))
for i in range(1,n+1):
    if i%2 == 0:
        continue
    elif i%3!=0:
        continue
    c+=1
    s+=i
print(f'A soma de todos os {c} valores solicitados é {s}')




