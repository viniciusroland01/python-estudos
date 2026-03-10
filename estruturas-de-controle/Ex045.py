#Game PEDRA PAPEL E TESOURA

from random import choice
from colorama import init, Fore, Back
from time import sleep

init(autoreset=True)

print('>'*23)
print(Back.BLACK + Fore.GREEN + 'Vamos jogar JOKENPÔ?')
print('<'*23)
print('')

lista=['pedra','papel','tesoura']

while True:

    computador = choice(lista)
    resposta=str(input('Escolha um: PEDRA, PAPEL, TESOURA OU "sair" para encerrar:')).lower().strip()
    if resposta == 'sair':
        print(Fore.RED + 'Encerrando . . .')
        break
    if resposta not in lista:
        print(Fore.RED + 'Valor incorreto!')
        continue
    print(Fore.GREEN + Back.BLACK + ' JÓ ')
    sleep(0.5)
    print(Fore.GREEN + Back.BLACK + ' KEN ')
    sleep(0.5)
    print(Fore.GREEN + Back.BLACK + ' PÔ !!!')
    sleep(1)

    if resposta == computador:
        print(Fore.YELLOW + 'Empate!')
    elif resposta == 'papel' and computador == 'pedra':
        print(Fore.GREEN + 'Jogador venceu!')
    elif resposta == 'papel' and computador == 'tesoura':
        print(Fore.RED + 'Computador venceu!')
    elif resposta == 'pedra' and computador == 'tesoura':
        print(Fore.GREEN + 'Jogador venceu!')
    elif resposta == 'pedra' and computador == 'papel':
        print(Fore.RED + 'Computador venceu!')
    elif resposta == 'tesoura' and computador == 'papel':
        print(Fore.GREEN + 'Jogador venceu!')
    elif resposta == 'tesoura' and computador == 'pedra':
        print(Fore.RED + 'Computador venceu!')
    else:
        print('Inválido')
    print(f'Computador= {Fore.YELLOW + computador.title() + Fore.RESET}  Jogador= {Fore.YELLOW + resposta.title()}')