#Aluguel de carros

while True:
    d=input('Quantos dias o carro ficou alugado? "sair" para encerrar...')
    if d.lower()=='sair':
        print('Encerrando . . . ')
        break
    else:
        try:
            dias=float(d)
            km=input('Quantos km foram percorridos? ')
            kilo=float(km)
            pagar=(dias*60)+(kilo*15/100)
            print(f'O total a pagar é R${pagar:.2f}')
        except ValueError:
            print('Inválido!')


