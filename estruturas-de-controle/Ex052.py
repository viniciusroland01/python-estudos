#Números primos

while True:
    n=int(input('Digite um número para saber se ele é primo: '))
    primo=True
    for i in range (2,n-1):
        if n % i == 0:
            primo=False
    if primo:
        print(f'O número {n} é primo')
    else:
        print(f'O número {n} não é primo')
    if n == 'sair':
        break



