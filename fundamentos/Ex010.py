#Conversor de moedas

while True:
    n=input('Digite o valor a ser convertido para dólar, ou (sair) para encerrar: ')
    if n.lower()=='sair':
        print('Encerrando programa...')
        break
    else:
        try:
            e=float(n)
            print(f'{n} equivale a {e/3.27:.2f} USD.')
        except ValueError:
            print('Entrada inválida.')


