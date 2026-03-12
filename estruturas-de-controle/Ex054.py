from datetime import datetime
atual=datetime.now().year
maiores=0
menores=0
for ano in range(0,10):
    idade=int(input('Ano de nascimento dos 10 participantes: '))
    if atual - idade >= 18:
        print('Maior de idade')
        maiores+=1
    else:
        print('Menor de idade!')
        menores+=1
print(f'A quantidade de maiores é {maiores} e a de menores é {menores}.')


