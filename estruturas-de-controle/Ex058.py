from random import choice

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
