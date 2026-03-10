#Tabuada v2.0

n=int(input('Digite um número para saber a sua tabuada: '))
print(f'A tabuada do {n} é: ')
for i in range (0,11):
    t=n*i
    print(f'{n} x {i} = {t} ')
