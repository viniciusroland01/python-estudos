#Analisando triângulo v1.0

from colorama import init, Fore
from time import sleep
while True:
    init(autoreset=True)
    print(Fore.RED + '-='*10)
    print('Analisador de Triângulos')
    print(Fore.RED + '-='*10)
    print('')
    reta1=input('Comprimento da primeira reta:')
    if reta1.lower() == 'sair':
        print(Fore.RED + 'Encerrando . . .')
        break
    try:
        reta1=float(reta1)
        reta2=float(input('Comprimento da segunda reta:'))
        reta3=float(input('Comprimento da terceira reta:'))
        print(Fore.LIGHTMAGENTA_EX + 'Analisando. . . ')
        sleep(1)
        if reta1+reta2>reta3 and reta2+reta3>reta1 and reta1+reta3>reta2:
            print(Fore.GREEN + 'Pode formar um triângulo!')
        else:
            print(Fore.RED + 'Não é possível formar um triângulo!')
    except ValueError:
        print('Inválido!')