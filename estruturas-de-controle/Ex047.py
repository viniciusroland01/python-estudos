#Contagem de pares

n1=int(input('Digite um número para saber quantos números pares até ele: '))
print(f'Os números pares de 0 a {n1} são :')
for c in range (0,n1+1,2):
    print(c,end=' ')
print('Finish!')

#n1=int(input('Digite um número para saber quantos números pares até ele: '))
#print(f'Os números pares de 0 a {n1} são :')
#for n in range (1,n1+1):
#    if n%2==0:
#        print(n,end= ' ')