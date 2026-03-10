#Gerenciador de pagamentos

while True:
    print('')
    print(f'{'='*10} Loja da Fernanda <3 {'='*10}')
    print('')
    preco=input('Qual o valor do produto? ')
    if preco.lower() == 'sair':
        print('')
        print('Encerrando . . .')
    try:
        preco=float(preco)
        pag=int(input('''Pagamento  
OPÇÃO1 = À VISTA/DINHEIRO (10% DE DESCONTO)
OPÇÃO2 = À VISTA NO CARTÃO (5% DE DESCONTO)
OPÇÃO3 = 2x NO CARTÃO (PREÇO NORMAL)
OPÇÃO4 = 3X OU MAIS NO CARTÃO (20% DE JUROS)
        
DIGITE A OPÇÃO (1, 2, 3 ou 4) : '''))
        print('')
        if pag == 1:
            pag1 = preco - (0.1*preco)
        elif pag == 2:
            pag1 = preco - (0.05*preco)
        elif pag == 3:
            pag1 = preco
        elif pag == 4:
            pag1 = (preco*0.2) + preco
            numparcelas = float(input('Quantas parcelas?'))
            parcelas=(preco*1.2)/numparcelas
            print('')
            print(f'A sua compra sera parcelada em {numparcelas:.0f} X R${parcelas:.2f}.')
        else:
            print('Inválido!')
            continue
        print(f'O produto no valor de R${preco:.2f} nesse método de pagamento fica R${pag1:.2f}. ')

    except ValueError:
        print('Inválido! Erro de digitação.')
