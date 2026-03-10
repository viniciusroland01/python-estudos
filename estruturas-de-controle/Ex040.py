#Média de notas

while True:
    n1=input('Qual a primeira nota? ')
    if n1.lower() == 'sair':
        print('Encerrando . . . ')
        break
    n1=float(n1)
    n2=float(input('Qual a segunda nota? '))
    if n1 and n2 >=10:
        print('Nota inválida! Máx 10 pontos.')
        break
    media=(n1 + n2)/2
    if media <= 5:
        print('\033[1:30:41mReprovado!\033[m')
    elif 5 < media < 6.9:
        print('\033[1:31mRecuperação!\033[m')
    elif media >= 7:
        print('\033[1:32mAprovado!\033[m')
    print(f'Sua média foi {media:.2f}')