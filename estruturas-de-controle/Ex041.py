#Classificando atletas

from datetime import datetime
while True:
    atual=datetime.now().year
    ano=input('Qual o ano do atleta? ')
    if ano.lower() == 'sair':
        print('Encerrando . . .')
        break
    ano=int(ano)
    idade=atual-ano
    print(f'O atleta tem {idade} anos. ')
    categoria=''
    if idade <=9:
        categoria='MIRIM'
    elif 9 < idade <= 14:
        categoria='INFANTIL'
    elif 14 < idade <=19:
        categoria='JUNIOR'
    elif 19 < idade <= 25:
        categoria='SÊNIOR'
    elif idade > 25:
        categoria='MASTER'
    print(f'Classificação: {categoria}')
