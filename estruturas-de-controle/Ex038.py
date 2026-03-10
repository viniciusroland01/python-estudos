#Comparando números

while True:
    n1 = input('Digite o primeiro número: ')
    if n1.lower() == 'sair':
        print('Encerrando . . .')
        break
    n1=float(n1)
    n2=float(input('Digite o segundo número: '))
    if n1 > n2:
        print('O primeiro é maior.')
    elif n2 > n1:
        print('O segundo é maior.')
    elif n1 == n2:
        print('Os valores são iguais.')