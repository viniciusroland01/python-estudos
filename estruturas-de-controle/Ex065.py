soma = 0
quantidade = 0


while True:

    num = input('Digite um número inteiro, ou "sair": ')
    while num.lower() != 'sair' :
        soma += int(num)
        num = input('Digite um número inteiro, ou "sair": ')
        quantidade += 1

    if quantidade > 0:
        media=soma/quantidade
        print(f'Foram digitados {quantidade} números, e a média entre eles é {media}')

    resposta = input('Você quer continuar digitando números? (S/N)')
    if resposta.lower() == 'n' :
        break
    else:
        soma = 0
        quantidade = 0
print('Encerrando . . .')





