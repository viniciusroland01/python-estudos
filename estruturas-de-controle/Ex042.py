#Analisador de triângulos v2.0

from time import sleep
from colorama import init, Fore, Back
init(autoreset=True)
print(Fore.RED + '~'*25)
print(Back.WHITE + Fore.BLACK + 'Analisador de Triângulos')
print(Fore.RED + '~'*25)
print('')
while True:
    try:
        r1=input('Comprimento da primeira reta: ')
        if r1.lower() == 'sair' :
            print('Encerrando. . . ')
            break
        r1=float(r1)
        r2=float(input('Comprimento da segunda reta: '))
        r3=float(input('Comprimento da terceira reta: '))
    except ValueError:
        print('Inválido!')
        continue
    print('')
    print(Fore.MAGENTA + 'Analisando . . .')
    print('')
    sleep(1)
    if r1 <= 0 or r2 <= 0 or r3 <= 0:
        print('Os valores devem ser positivos!')
        print('')
    if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
        if r1 == r2 == r3:
            form='Equilátero'
        elif r1 != r2 != r3 != r1:
            form='Escaleno'
        else:
            form='Isósceles'
        print(Fore.GREEN + f'É possível formar um triângulo! Esse triângulo é {form}')
        print('')
    else:
        print(Fore.RED + 'Não é possível formar um triângulo!')
        print('')



