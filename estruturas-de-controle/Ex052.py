#Números primos

#while True:
#    n=int(input('Digite um número para saber se ele é primo: '))
#    primo=True
#    for i in range (2,n-1):
#        if n % i == 0:
#            primo=False
#
#    if primo:
#        print(f'O número {n} é primo')
#    else:
#        print(f'O número {n} não é primo')
#    if n == 'sair':
#        break

while True:
    n = int(input('Digite um número para saber se ele é primo: '))
    t=0
    for c in range (1, n + 1):
        if n % c == 0 :
            print('\033[31m' , end='')
            t += 1
        else:
            print('\033[m' , end='')
        print(f'{c} ' , end= '')
    print('\033[m')
    if t == 2:
        print('É primo!')
    else:
        print('Não é primo')
    print()



