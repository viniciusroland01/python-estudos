escolha = 0
n1=int(input('Digite o primeiro número: '))
n2=int(input('Digite o segundo número: '))

while escolha != 5:
        print('''
Escolha as opcões : 
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
''')
        escolha=int(input('Escolha:'))

        if escolha == 1:
            print(f'A soma entre {n1} e {n2} é igual a {n1+n2}')

        elif escolha == 2:
            print(f'A multiplicação entre {n1} e {n2} é igual a {n1*n2}')

        elif escolha == 3:
            if n1 > n2 :
                maior = n1
                print(f'O maior número é : {maior}')
            elif n2 > n1:
                maior = n2
                print(f'O maior número é : {maior}')
            else:
                print('Os números são iguais.')

        elif escolha == 4:
            print('Escolhendo novos números.')
            n1 = int(input('Digite o primeiro número: '))
            n2 = int(input('Digite o segundo número: '))

        elif escolha == 5:
            print('Encerrando programa. . .')
        else:
            print('Inválido')




