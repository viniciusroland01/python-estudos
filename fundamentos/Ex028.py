#Jogo da adivinhação v1.0

from random import choice
from time import sleep
from colorama import Fore, init, Back
init(autoreset=True)
print('-=-' * 20)
print(Fore.GREEN + Back.BLACK +'Vou pensar em um número de 0 a 5, tente adivinhar. . .')
print('-=-' * 20)
while True:
    num=[0,1,2,3,4,5]
    sort=choice(num)
    usu=input(Fore.GREEN + 'Em que número eu pensei? ')
    if usu.lower() == 'sair':
        print(Fore.LIGHTRED_EX + 'Encerrando programa. . .')
        break
    elif int(usu) > 5:
        print(Fore.RED + 'O número tem que estar entre 0 e 5!')
        continue
    try:
        print(Fore.LIGHTMAGENTA_EX + 'Processando . . .')
        sleep(1)
        usu=int(usu)
        if usu == sort:
            print(Fore.LIGHTYELLOW_EX + 'Você ganhou o sorteio!')
            print('')
        else:
            print(Fore.LIGHTRED_EX + f'Não foi dessa vez! Eu pensei no número {sort}, tente denovo!')
            print('')
    except ValueError:
        print('Inválido!')

'''from random import randint
comp = randint(0,5)
print('-=-'*20)
print('Vou pensar em um número de 0 a 5, tente adivinhar!')
print('-=-'*20)
jog=int(input('Em que número eu pensei?'))
if jog == comp:
    print('Você acertou!')
else:
    print(f'Eu ganhei! Pensei no número {comp} não no {jog}!')'''




