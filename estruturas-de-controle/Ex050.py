#Soma apenas de números pares

s=0
n1=int(input('Digite seis números inteiros:'))
if n1 % 2 == 0:
    s+=n1
for n in range(0,5):
    n2=int(input('Mais um:'))
    if n2 % 2 == 0:
        s+=n2
print(s)
