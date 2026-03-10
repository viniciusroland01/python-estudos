#Quebrando um número

while True:
    n=input('Digite um valor: ')
    if n.lower()=='sair':
        print('Encerrando. . . ')
        break
    else:
        try:
            n1=float(n)
            print(f'A parte inteira do número {n1} é {int(n1)}')
        except ValueError:
            print('Inválido!')


