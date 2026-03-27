#Jogo da Adivinhação v2.0

from random import randint

sorteio = randint(0, 10)
tentativas = 0
acertou = False

print('Sou seu computador. Pensei em um número entre 0 e 10')
print(f'Será que você consegue adivinhar? {sorteio}')

while not acertou:

    jogador = int(input('Qual o seu palpite?'))

    if jogador not in range(0, 11):
        print('Dica: está entre 0 e 10. Tente novamente.')
        tentativas += 1

    if jogador == sorteio:
        acertou = True
        tentativas += 1

    else:
        if jogador > sorteio:
            print('Menos... Tente novamente')
            tentativas += 1
        elif jogador < sorteio:
            print('Mais... Tente novamente')
            tentativas += 1

print(f'Você acertou e precisou de {tentativas} tentativas.')

'''from random import choice

lista_num=[0,1,2,3,4,5,6,7,8,9,10]
sorteio=choice(lista_num)

jogador=0
tentativas=0

print('Pensei em um número entre 0 e 10.  ')

while jogador != sorteio :
    jogador = int(input('Tente adivinhar o número que pensei: '))
    if jogador != sorteio :
        print('Tente novamente')
        tentativas =+ 1
    if jogador == sorteio :
        tentativas =+ 1
        print(f'Você acertou! {tentativas} tentativas foram usadas')
        break




from random import choice

lista_num=[0,1,2,3,4,5,6,7,8,9,10]
sorteio=choice(lista_num)
jogador = 0
tentativas = 0

print('Pensei em um número entre 0 e 10. ')
jogador = int(input('Tente adivinhar o número que pensei: '))

while jogador > sorteio:
    jogador = int(input('Menos... Tente mais uma vez.'))
    tentativas += 1
while jogador < sorteio:
    jogador = int(input('Mais... Tente mais uma vez.'))
    tentativas += 1
if jogador == sorteio :
    tentativas += 1
    print(f'Acertou! Você precisou de {tentativas} tentativas.')'''






