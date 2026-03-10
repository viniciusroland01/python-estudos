#Alistamento militar

from datetime import datetime
while True:
    atual = datetime.now().year
    ano = input('Qual o ano de nascimento? ')
    if ano.lower() == 'sair':
        print('Encerrando . . . ')
        break
    ano = int(ano)
    idade = atual - ano
    correto = ano + 18
    if idade < 18:
        print(f'Você tem {idade} anos, vai se alistar no ano {correto} e faltam {18 - (atual-ano)} anos.')
    elif idade > 18:
        print(f'Se não alistou, você está atrasado {atual - correto} anos! Você tem {idade} anos e era para ter se alistado em {correto}')
    else:
        print(f'Está na hora de se alistar! Você tem {idade} anos')

