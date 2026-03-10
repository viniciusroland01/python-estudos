#Ano bissexto

from datetime import datetime
while True:
    atual=datetime.now().year
    ano=input('Digite um ano qualquer, ou "atual" para saber se é BISSEXTO:  ')
    if ano.lower()=='sair':
        print('Encerrando . . .')
        break
    try:
        if ano.lower() == 'atual':
            ano=atual
        ano=int(ano)
        if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
            print(f'O ano {ano} é bissexto')
        else:
            print(f'O ano {ano} não é bissexto')
    except ValueError:
        print('Inválido!')
